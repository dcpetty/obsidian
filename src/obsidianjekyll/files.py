#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# files.py
#
"""
files.py defines Files class with copy_files function and files, paths, and
pathnames properties.
"""

__all__ = ["Files", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

import os, pathlib, re, shutil, time, yaml
from paths import Paths
from log import log

# Set up logging.
logger = log(__name__, 'obsidian')


class Files(object):
    """Process files into list of dictionaries contaning keys:
    note_path - full repository note pathname
    note_file - repository note filename
    note_relp - note pathname relative to repo used for permalink or asset copy
    note_ctime- note creation time
    note_mtime- note modification time
    note_ismd - True if note_path is a .MD file, otherwise it's an asset file
    note_text - list of lines of text in repository file
    note_yaml - repository YAML front matter
    post_path - full post pathname paths.post_path(note_path, yaml_date)
                or paths.asset_path(post_path)
    post_mtime- post modification time (if post exists)
    """

    _default_files = list()


    def __init__(self, path_names):
        """Initialize _path_names, _paths, _files."""
        self._path_names = path_names
        self._paths = path_names.paths
        self._files = type(self)._default_files

        # Initialize all pathnames into file dictionaries.
        for path in self.path_names.path_names:
            self._add_file(path)

        self._log()


    def _log(self):
        # logger.debug(f"paths: {self.paths}")        # Paths logs
        # logger.debug(f"names: {self.path_names}")   # PathNames logs
        # Log file dictionaries' relevant information
        for fd in self.files:
            exc = { 'front', 'lines', } # exclude values for these keys
            fd_text = '\n  '.join([f"{k}: {v}"
                for k, v in fd.items() if k not in exc])
            logger.debug(f"file: "
                f"'{self.paths.rel_note_path(fd['note_path'])}'\n  {fd_text}")


    # Properties paths, path_names, files.
    def _get_paths(self): return self._paths
    paths = property(_get_paths)
    def _get_path_names(self): return self._path_names
    path_names = property(_get_path_names)
    def _get_files(self): return self._files
    files = property(_get_files)


    _yaml_datetime = lambda timestamp: \
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    _yaml_date = lambda timestamp: \
        time.strftime('%Y-%m-%d', time.localtime(timestamp))


    def _add_file(self, note_path):
        """Add repository file dictionary for pathname to _files."""
        repo_path, site_path = self.paths.repo_path, self.paths.site_path
        assert os.path.isfile(note_path), f"'{note_path}' does not exist"
        assert note_path.startswith(repo_path), \
            f"not '{note_path}'.startswith('{repo_path}')"

        file_dict = dict()
        file_dict['note_path'] = note_path
        file_dict['note_file'] = self.paths.note_filename(note_path)
        file_dict['note_relp'] = self.paths.rel_note_path(note_path)

        # Set file times.
        has_birthtime = hasattr(os.stat(note_path), 'st_birthtime')
        note_stat = \
            os.stat(note_path) \
                if has_birthtime else pathlib.Path(note_path).stat()
        file_dict['note_ctime'] = note_stat.st_birthtime \
            if has_birthtime else note_stat.st_ctime
        file_dict['note_mtime'] = os.path.getmtime(note_path)

        # Parse .MD files. Others are untouched.
        file_dict['is_md'] = os.path.splitext(note_path)[1].lower() == '.md'

        if file_dict['is_md']:
            # Process .MD file.
            file_dict['post_path'] = self.paths.post_path(note_path,
                Files._yaml_date(file_dict['note_ctime']))
            if os.path.isfile(file_dict['post_path']):
                file_dict['post_mtime'] = os.path.getmtime(file_dict['post_path'])
            # Parse file into front, lines, and yaml added to file_dict.
            self._parse_md(file_dict)
        else:
            # Process asset file.
            file_dict['post_path'] = self.paths.asset_path(note_path)
            if os.path.isfile(file_dict['post_path']):
                file_dict['post_mtime'] = os.path.getmtime(file_dict['post_path'])

        self.files.append(file_dict)


    def _parse_md(self, file_dict):
        """Parse YAML front matter lines (if any) to file_dict['front'] and
        list of other lines (if any) to file_dict['lines']. Then add
        file_dict['yaml'] with the merged front matter and Jekyll information
        in file_dict. file_dict str keys include: note_path, note_file,
        note_ctime, note_mtime, is_md."""
        assert file_dict['is_md'], \
            f"'{file_dict['note_file']}' is not a markdown file"
        front, lines, in_yaml, divider = list(), list(), False, None

        # Read lines of note_path and parse into YAML front matter and text lines.
        with open(file_dict['note_path'], encoding='utf-8') as np:
            for line in np.readlines():
                # Process YAML .MD file, looking for lines starting '---'
                if line.startswith('---'):
                    in_yaml = not in_yaml   # toggle in_yaml
                    if in_yaml and divider:
                        front.append(divider)
                    divider = '---\n'
                else:
                    if in_yaml:
                        front.append(line)  # add line to front matter
                    else:
                        fixed = self._reformat_links(line.rstrip(), self.paths.repo)
                        lines.append(fixed) # add fixed line to text lines

        # Add front, lines, and yaml to file_dict.
        file_dict['front'] = front
        file_dict['lines'] = lines
        file_dict['yaml'] = self._parse_yaml(file_dict) # updates lines


    def _reformat_links(self, line, repo):
        """Replace local links in line with corrected slugified links.
        First
        - search for '(repo/dir/file.ext)'
        - replace 'repo/' with '/repo/'
        - if ext is '.md', remove it
        - slugify the new link (assumes asset dirnames are already slugified)
        - substitute it for the old link
        - iterate for all matching links
        Second:
        - search for '[[link]]' that is not immediately preceded or followed by '`'
        - replace '[[link]]' with '[link](link)'
        - iterate for all matching links
        - return fixed line
        """

        # Process single-bracket links everywhere on line.
        single_re = re.compile(f"([(]{repo}/[^)]*" + r'[.]\w{2,4}[)])+')
        fixed = line[:]
        for match in single_re.finditer(line):
            old_link = line[match.start(): match.end()]
            #logger.info(f"match: {line[match.start() + 1: match.end() - 1]}")
            new_link = re.sub('[.]md$', '', re.sub(f"^{repo}/", f"/{repo}/",
                Paths.slugify(line[match.start() + 1: match.end() - 1])))
            #logger.info(f"new link:  '{new_link}'")
            fixed = fixed.replace(old_link, f"({new_link})")
            #logger.info(f"fixed '[': '{fixed.strip()}'")

        # Process double-bracket links everywhere on fixed line.
        double_re = re.compile(r'((^|[^`])([\[]{2}([^\]]*)[\]]{2})([^`]|$))+')
        for match in double_re.finditer(fixed):
            old_link = match.groups()[2]
            uri = match.groups()[3]
            new_link = f"[{uri}]({uri})"
            fixed = fixed.replace(old_link, new_link)
            # logger.debug(f"fixed '[[': {fixed.strip()}")

        return fixed

    def _parse_yaml(self, file_dict):
        """Return consolidated YAML dictionary parsed from existing YAML
        collected from file_dict['front'] (if any) and formatted Jekyll YAML
        parsed from file_dict['lines'] --- which may be updated if initial H1
        title removed. file_dict str keys include: front, lines, note_path,
        note_file, note_ctime, note_mtime."""
        front, lines, jekyll = file_dict['front'], file_dict['lines'], dict()

        # The YAML of a Jekyll should have:
        # - title: parsed from the first h1 line which is the removed or note filename
        # - date: creation date
        # - last_modified_at: modification date
        # - show_date: true
        # - permalink: slugified note filename relative to repo minus extension
        # - tags: parsed from hashtags in lines
        # - toc: true if any headers (r'^[#]{1,6}\s') in lines
        # - toc_sticky: true if any headers (r'^[#]{1,6}\s') in lines
        jekyll['title'] = self._parse_title(lines,
            os.path.splitext(file_dict['note_file'])[0])
        jekyll['date'] = Files._yaml_datetime(file_dict['note_ctime'])
        jekyll['last_modified_at'] = Files._yaml_datetime(file_dict['note_mtime'])
        jekyll['show_date'] = 'true'
        jekyll['permalink'] = self.paths.permalink(file_dict['note_path'])
        tag_list = self._parse_tags(lines)
        if tag_list:
            jekyll['tags'] = tag_list
        if self._has_headers(lines):
            jekyll['toc'] = 'true'
            jekyll['toc_sticky'] = 'true'
        yaml_dict_list = [jekyll] + list(yaml.safe_load_all(''.join(front)))
        # logger.debug(f"yamls: {yaml_dict_list}")
        return self._merge_yaml(yaml_dict_list)


    def _parse_title(self, lines, alt='TITLE'):
        """Return title parsed from first non-blank line of lines if it is an
        H1, otherwise alt."""
        title = alt
        for i, line in enumerate(lines):
            if not line: continue       # skip leading blank lines
            if line.startswith('# '):   # extract title from first heading1
                title = line[2:].strip()
                del lines[i]
            break                       # otherwise break
        return title


    def _parse_tags(self, lines):
        """Return list of tags parsed from lines."""
        tags = list()
        for line in lines:
            tags += [h.strip()[1:]
                for h in re.findall(r'[#][\w-]+\s', f"{line} ")]
        return tags


    def _has_headers(self, lines):
        """Return True if there are any H1 - H6 lines in lines. Must come after
        _parse_title so after any initial H1 title is removed. Used to determine
        whether table of contents should be included."""
        regex = re.compile(r'^[#]{1,6}\s')
        for line in lines:
            if regex.search(line):
                return True
        return False


    def _merge_yaml(self, yaml_list):
        """Return dictionary of yaml_list dictionaries merged into one
        where values for every key are either the concatenation of all strings,
        or a set of the union of list values for duplicate keys sorted."""
        merged = dict()
        for yaml_dict in yaml_list:
            for key in yaml_dict:
                # yaml_dict[key] is list or str.
                empty = list() if isinstance(yaml_dict[key], list) else ''
                merged[key] = merged.get(key, empty) + yaml_dict[key]
        return { key: sorted(set(val)) if isinstance(val, list) else val
            for key, val in merged.items() }


    # TODO fix _fix_yaml to be more specific to 'true' or '2024-03-25 18:15:12'
    _fix_yaml = lambda s: \
        re.sub('(title: )(.*)', r'\1"\2"',  # put '"' around title
        re.sub(': [\'"]', ': ',             # remove quotes after ': '
        re.sub('[\'"]\n', '\n', s)))        # remove quotes before '\n'


    def copy_files(self):
        """Copy all files in self.files. """
        for fd in self.files:
            # Initialize local variables.
            note_path, note_mtime = fd['note_path'], fd['note_mtime']
            post_path = fd['post_path']
            post_dirname = os.path.dirname(fd['post_path'])
            note_changed = not os.path.isfile(post_path) \
                or note_mtime > fd['post_mtime']
            if note_changed:
                if fd['is_md']:
                    # Write markdown file after 'fixing' YAML.
                    lines = fd['lines']
                    yaml_text = Files._fix_yaml(yaml.safe_dump(fd['yaml'],
                        default_style=None, default_flow_style=False,
                        sort_keys=False, allow_unicode=True))
                    div, nl = '---\n', '\n'
                    # Create directory and write post.
                    os.makedirs(post_dirname, exist_ok=True)
                    with open(post_path, "w", encoding='utf-8') as wf:
                        wf.write(f"{div}{yaml_text.strip()}{nl}{div}")
                        wf.write('\n'.join(lines).lstrip())
                    logger.info(f"{note_path} \u2192 {post_path}")
                else:
                    # Create directory and copy asset file.
                    os.makedirs(post_dirname, exist_ok=True)
                    shutil.copy(note_path, post_path)
                    logger.info(f"{note_path} \u2192 {post_path}")
            else:
                logger.debug(f"UNCHANGED: {note_path}")
