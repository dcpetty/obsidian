#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# obsidianjekyll.py
#
"""
obsidian.py copies a REPODIR Obsidian repository to a POSTDIR Jekyll repository,
modifying the pathnames appropriately.

TODO: complete this description
"""

__version__ = "0.0.3"

__all__ = ["main", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

import argparse, log, os, re, sys
import datetime, fnmatch, glob, pathlib, shutil, time, unicodedata, yaml

# Set up logging.
logger = log.log(__name__, 'obsidian')


class Paths(object):
    """Keep track of the directories, paths, and repository."""

    _default_repodir = '.'
    _default_postdir = './docs'


    def __init__(self, repodir=None, postdir=None):
        """Initialize paths for repository and site."""
        self._repodir = repodir if repodir else type(self)._default_repodir
        self._postdir = postdir if postdir else type(self)._default_postdir
        self._repo_path = os.path.realpath(self._repodir)   # no trailing '/'
        self._repo = os.path.normpath(self._repo_path).split(os.sep)[-1]
        self._site_path = os.path.realpath(self._postdir)   # no trailing '/'
        self._posts_path = os.path.join(self.site_path, '_posts')

        assert os.path.isdir(self._repo_path), \
            f"'{self._repo_path}' is not a directory"
        assert os.path.isdir(self._site_path), \
            f"'{self._site_path}' is not a directory"
        assert os.path.exists(self._posts_path) \
            and os.path.isdir(self._posts_path), \
            f"'{self._posts_path}' is not a directory"

        self._log()


    def _log(self):
        logger.debug(f"Paths repo_path:  {self.repo_path}")
        logger.debug(f"Paths repo:       {self.repo}")
        logger.debug(f"Paths site_path:  {self.site_path}")
        logger.debug(f"Paths posts_path: {self.posts_path}")
        #logger.info(f"perma: {self.permalink(os.path.join(self.repo_path, 'TestPages/This is a note with spaces,_ éh? !@$-.md'))}")
        #logger.info(f"post:  {self.post_path(os.path.join(self.repo_path, 'TestPages/This is a note with spaces,_ éh? !@$-.md'), '2024-03-22')}")
        #logger.info(f"asset: {self.asset_path(os.path.join(self.repo_path, 'assets/obsidian/Pasted image 20240326090137.png'))}")


    # Properties repo_path, repo, site_path, posts_path.
    def _get_repo_path(self): return self._repo_path
    repo_path = property(_get_repo_path)
    def _get_repo(self): return self._repo
    repo = property(_get_repo)
    def _get_site_path(self): return self._site_path
    site_path = property(_get_site_path)
    def _get_posts_path(self): return self._posts_path
    posts_path = property(_get_posts_path)


    # Utilities for note_path.
    def _check_dir(self, d): assert os.path.isdir(d), f"'{d}' is not a directory"; return d
    def _check_file(self, f): assert os.path.isfile(f), f"'{f}' is not a file"; return f
    def note_dirname(self, note_path): return self._check_dir(os.path.dirname(note_path))
    def note_filename(self, note_path): return os.path.basename(self._check_file(note_path))
    def rel_note_path(self, note_path): return self._check_file(note_path).replace(f"{self.repo_path}/", '')
    def rel_note_dirname(self, note_path): return os.path.dirname(self.rel_note_path(note_path))
    def permalink(self, note_path): return f"/{os.path.splitext(self.slugify(self.rel_note_path(note_path)))[0]}/"
    def post_path(self, note_path, yaml_date): return os.path.join(self.posts_path,
        f"{yaml_date}-{self.slugify(self.note_filename(note_path))}")
    def asset_path(self, note_path): return os.path.join(self.site_path,
        self.rel_note_dirname(note_path), self.slugify(self.note_filename(note_path)))


    @staticmethod
    def slugify(path, preserve_case=False):
        """Return simple slugified path. Used to slugify paths and links. If
        preserve_case is False, convert slugified path to lowercase.
        - split off any extension and work with root
        - replace '%20' with ' '
        - unicodedata.normalize 'NFKD'
        - remove everything *not* letters, numerals, or '/._-'
        - replace ' ' or '.' or '_' with '-' (Jekyll)
        - remove duplicate '-'s (Jekyll)
        - add back on the extension
        """
        # https://stackoverflow.com/a/27264385
        root, ext = os.path.splitext(path)
        slugified = re.sub('[-]{2,}', '-',
            re.sub(r'[\s._]', '-', re.sub(r'[^/\w\s._-]', '',
                unicodedata.normalize('NFKD', re.sub(r'%20', ' ', root))
                    .encode('ascii', 'ignore').decode('ascii')))) \
                        .strip('-') + ext
        return slugified if preserve_case else slugified.lower()


class PathNames(object):
    """Collect Jekyll file pathnames from an Obsidian vault."""

    # List of patterns to include.
    _default_to_inc = ['*.md', '*.png', '*.jpg', '*.html', ]
    # List of patterns to exclude.
    _default_to_exc = ['**/.git/**', '**/docs/**', '**/scripts/**', '**/README.md',
        '**/foo/**/bar/*.html']  # TODO: this is simply to test valid_paths

    def __init__(self, paths, to_inc=None, to_exc=None):
        """Created sorted list of valid paths below repo_path."""
        self._paths = paths
        self._to_inc = to_inc if to_inc else type(self)._default_to_inc
        self._to_exc = to_exc if to_exc else type(self)._default_to_exc
        self._path_names = self._valid_paths(self.paths.repo_path, self._to_inc, self._to_exc)

        self._log()


    def _log(self):
        # logger.debug(f"PathNames paths:       {self.paths}")
        # logger.debug(f"PathNames path_names:  {self.path_names}")
        pass    # Paths and self._valid_paths already log


    # Properties paths, path_names.
    def _get_paths(self): return self._paths
    paths = property(_get_paths)
    def _get_path_names(self): return self._path_names
    path_names = property(_get_path_names)


    def _valid_paths(self, repo_path, to_inc, to_exc):
        """Return sorted list of valid paths below repo_path if matching to_inc,
        but not if matching to_exc. logging.DEBUG the result."""

        # https://stackoverflow.com/a/5141829
        # glob all *.* paths below repo_path.
        all_paths = [p for p in glob.glob(os.path.join(repo_path, '**/*.*'),
            recursive=True)]

        # Transform glob patterns to regular expressions.
        nonpath = '/:GLOB:/'    # nonpath cannot be part of a pathname
        wc_regex = lambda glob: fnmatch.translate(glob.replace('**/', nonpath)) \
            .replace(nonpath, '(.*/)*')
        inc_regex = r'|'.join([wc_regex(x) for x in to_inc])
        exc_regex = r'|'.join([wc_regex(x) for x in to_exc]) or r'$.'

        # Create set of all includable paths matching inc_regex.
        included = {p for p in all_paths if re.match(inc_regex, p)}
        # Create set of valid paths that does not include paths matching exc_regex.
        paths = sorted({p for p in included if not re.match(exc_regex, p)})

        def _log_valid_paths():
            logger.debug(f"PathNames include regex:    {inc_regex}")
            logger.debug(f"PathNames exclude regex:    {exc_regex}")
            logger.debug(f"PathNames         included: {included}")
            logger.debug(f"PathNames and not excluded: {paths}")
            # Log each valid path to process relative to repo_path.
            for path in paths:
                valid_pathname = path.replace(repo_path + '/', '')
                logger.debug(f"PathNames valid:        {valid_pathname}")

        _log_valid_paths()

        return paths

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
        # logger.debug(f"Files paths: {self.paths}")        # Paths logs
        # logger.debug(f"Files names: {self.path_names}")   # PathNames logs
        # Log file dictionaries' relevant information
        for fd in self.files:
            exc = { 'front', 'lines', } # exclude values for these keys
            fd_text = '\n  '.join([f"{k}: {v}"
                for k, v in fd.items() if k not in exc])
            logger.debug(f"Files file: "
                f"'{self.paths.rel_note_path(fd['note_path'])}'\n  {fd_text}")


    # Properties paths, path_names, files.
    def _get_paths(self): return self._paths
    paths = property(_get_paths)
    def _get_path_names(self): return self._path_names
    path_names = property(_get_path_names)
    def _get_files(self): return self._files
    files = property(_get_files)


    yaml_datetime = lambda timestamp: \
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
    yaml_date = lambda timestamp: \
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
                Files.yaml_date(file_dict['note_ctime']))
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

        # Add fron, lines, and yaml to file_dict.
        file_dict['front'] = front
        file_dict['lines'] = lines
        file_dict['yaml'] = self._parse_yaml(file_dict) # updates lines


    def _reformat_links(self, line, repo):
        """Replace local links in line with corrected slugified links.
        First
        - search for '(repo/dir/file.ext)'
        - replace 'repo/' with '/repo/'
        - if ext is '.md', remove it
        - slugify the new link (assumes asset pathnames are already slugified)
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
        jekyll['date'] = Files.yaml_datetime(file_dict['note_ctime'])
        jekyll['last_modified_at'] = Files.yaml_datetime(file_dict['note_mtime'])
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


    # TODO fix fix_yaml to be more specific to 'true' or '2024-03-25 18:15:12'
    fix_yaml = lambda s: \
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
            if fd['is_md']:
                # Write markdown file after 'fixing' YAML.
                if note_changed:
                    lines = fd['lines']
                    yaml_text = Files.fix_yaml(yaml.safe_dump(fd['yaml'],
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
                    logger.debug(f"UNCHANGED: {note_path}")
            else:
                # Copy asset file.
                if note_changed:
                    # Create directory and copy post.
                    os.makedirs(post_dirname, exist_ok=True)
                    shutil.copy(note_path, post_path)
                    logger.info(f"{note_path} \u2192 {post_path}")
                else:
                    logger.debug(f"UNCHANGED: {note_path}")


def prepare(REPODIR, POSTDIR, REBUILD=False):
    """Copy and modify valid paths from REPODIR to POSTDIR. If REBUILD, remove
    _posts and _site directories."""
    paths = Paths(REPODIR, POSTDIR) # initialize paths w/ REPODIR and POSTDIR

    # If REBUILD, clean _posts directory.
    if REBUILD and os.path.isdir(paths.posts_path):
        logger.debug(f"removing: {paths.posts_path}")
        shutil.rmtree(paths.posts_path, ignore_errors=True)
    # If REBUILD, clean _site directory. Jekyll should automatically handle.
    _site_path = os.path.join(paths.site_path, '_site')
    if REBUILD and os.path.isdir(_site_path):
        logger.debug(f"removing: {_site_path}")
        shutil.rmtree(_site_path, ignore_errors=True)

    # Collect paths to modify and copy.
    path_names = PathNames(paths)   # collect all valid Obsidian vault paths
    files = Files(path_names)       # process information from all paths
    files.copy_files()              # copy from Obsidian to Jekyll changed files


class Parser(argparse.ArgumentParser):
    """Create OptionParser to parse command-line options."""
    def __init__(self, **kargs):
        argparse.ArgumentParser.__init__(self, **kargs)
        # self.remove_argument("-h")
        self.add_argument("-?", "--help", action="help",
                          help="show this help message and exit")
        self.add_argument('--version', action='version',
                          version=f"%(prog)s {__version__}")

    def error(self, msg):
        sys.stderr.write("%s: error: %s\n\n" % (self.prog, msg, ))
        self.print_help()
        sys.exit(2)


def main(argv):
    """Parse arguments and move files into Jekyll format."""
    description = """Format files in REPODIR into Jekyll and copy results
        to POSTDIR."""
    formatter = lambda prog: \
        argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=30)
    parser = Parser(description=description, add_help=False,
                    formatter_class=formatter)
    arguments = [
        # c1, c2, action, dest, default, help
        ('-r', '--rebuild', 'store_true', 'REBUILD', False,
         'rebuild entire Jekyll site', ),
        ('-v', '--verbose', 'store_true', 'VERBOSE', False,
         'log DEBUG status information',),
    ]

    # Add optional arguments with values.
    for c1, c2, a, v, d, h in arguments:
        parser.add_argument(c1, c2, action=a, dest=v, default=d, help=h,)

    # Add positional arguments. 'NAME' is both the string and the variable.
    parser.add_argument("REPODIR", help="repository source directory")
    parser.add_argument("POSTDIR", help="posts destination directory")

    # Parse arguments.
    pa = parser.parse_args(args=argv[1: ])
    if pa.VERBOSE:
        logger.setLevel('DEBUG')
    if pa.REPODIR:
        logger.debug(f"REPODIR = '{pa.REPODIR}'")
    if pa.POSTDIR:
        logger.debug(f"POSTDIR = '{pa.POSTDIR}'")
    logger.debug(f"VERBOSE: '{log.log_path()}'")
    if pa.REBUILD:
        logger.debug(f"REBUILD Jekyll site...")

    prepare(pa.REPODIR, pa.POSTDIR, pa.REBUILD)


if __name__ == '__main__':
    is_idle, is_pycharm, is_jupyter = (
        'idlelib' in sys.modules,
        int(os.getenv('PYCHARM', 0)),
        '__file__' not in globals()
    )
    if any((is_idle, is_pycharm, is_jupyter,)):
        logger.debug(f"logpath: {log.log_path()}")
        tests = [
            ['obsidianjekyll.py', '..', '../docs/', ],
            # ['obsidianjekyll.py', '-?', ],
        ]
        # slugify test
        # value = 'obsidian/TestPages/Page%20for%20testing...%20_-_-_%20éh?%20!@$-.md'
        # logger.info((value, Paths.slugify(value, True),))
        for test in tests:
            logger.debug(f"# {' '.join(test)}")
            main(test)
    else:
        main(sys.argv)
