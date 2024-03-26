#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# obsidian.py
#
"""
obsidian.py copies a REPODIR Obsidian repository to a POSTDIR Jekyll repository,
modifying the pathnames appropriately.

TODO: complete this description
"""

__version__ = "0.0.2"

__all__ = ["main", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

import argparse, log, os, re, sys
import datetime, fnmatch, glob, pathlib, shutil, time, unicodedata

# Set up logging.
logger = log.log(__name__, 'obsidian')


def valid_paths(repo_path):
    """Return valid paths below repo_path."""

    # glob all *.* paths below repo_path.
    all_paths = [p for p in glob.glob(os.path.join(repo_path, '**/*.*'),
        recursive=True)]

    # https://stackoverflow.com/a/5141829
    # List of patterns to include.
    to_inc = ['*.md', '*.png', '*.jpg', '*.html', ]
    # List of patterns to exclude.
    to_exc = ['**/.git/**', '**/docs/**', '**/scripts/**', '**/README.md',
        '**/foo/**/bar/*.html'] # TODO: this is simply to test valid_paths

    # transform glob patterns to regular expressions
    nonpath = '/:GLOB:/'    # nonpath cannot be part of a pathname
    wc_regex = lambda glob: fnmatch.translate(glob.replace('**/', nonpath)) \
        .replace(nonpath, '(.*/)*')
    inc_regex = r'|'.join([wc_regex(x) for x in to_inc])
    logger.debug(f"include regex: {inc_regex}")
    exc_regex = r'|'.join([wc_regex(x) for x in to_exc]) or r'$.'
    logger.debug(f"exclude regex: {exc_regex}")

    # Create set of all includable paths matching inc_regex.
    included = {p for p in all_paths if re.match(inc_regex, p)}
    logger.debug(f"        included: {included}")
    # Create set of valid paths that does not include paths matching exc_regex.
    paths = {p for p in included if not re.match(exc_regex, p)}
    logger.debug(f"and not excluded: {paths}")

    # Log each valid path to process relative to repo_path.
    for path in paths:
        logger.debug(f"valid: {path.replace(repo_path + '/', '')}")

    return paths


# TODO: fix using permalink
def slugify(path, preserve_case=False):
    """Return simple slugified path. Used to slugify paths and links.
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


def format_yaml(title, repo, categories, tags, toc=False, path=None):
    """Return list of YAML front matter lines for title, [prefix] + categories,
    & tags. If path, logging.DEBUG the YAML front matter for path."""
    all_categories = [] + categories # include any prefixes
    categories_yaml = (['categories:'] + [f' - {c}' for c in all_categories]) \
        if all_categories else list()
    tags_yaml = (['tags:'] + [f' - {t}' for t in tags]) \
        if tags else list()
    toc_yaml = (['toc: true', 'toc_sticky: true', ]) \
        if toc else list()
    yaml = [
        f'---', 'show_date: true',
        f'title: "{title}"',
        ] + categories_yaml + tags_yaml + toc_yaml + [
        f'---', ''
    ]

    # Log YAML front matter for path.
    if path:
        logger.debug(f"format_yaml:\n"
            f"     (title)'{title}'\n"
            f"      (repo)'{repo}'\n"
            f"(categories)'{categories}'\n"
            f"      (tags)'{tags}'\n"
            f"YAML for '{path}'\n"
            f"{chr(10).join(yaml).strip()}")

    return yaml


def reformat_links(line, repo):
    """Replace local links in line with corrected slugified links.
    - search for '(repo/dir/file.ext)'
    - replace 'repo/' with '/repo/'
    - if ext is '.md', remove it
    - slugify the new link (assumes asset directories are already slugified)
    - substitute it for the old link
    - iterate for all links and return fixed line
    """
    regex, fixed = re.compile(f"([(]{repo}/[^)]*" + r'[.]\w{2,4}[)])+'), line[:]
    for match in regex.finditer(line):
        old_link = line[match.start():match.end()]
        new_link = slugify(line[match.start():
            match.end() - (4 if old_link.endswith('.md)') else 1)]
                .replace(f"({repo}/", f"(/{repo}/"))
        logger.debug(f"links: '{old_link}' '({new_link})'")
        fixed = fixed.replace(old_link, f"({new_link})")
        # logger.debug(f"fixed line: {fixed.strip()}")
    return fixed


def parse_tags(line):
    """Return list of tags parsed from line."""
    return [h.strip()[1:] for h in re.findall(r'[#]\w+\s', f"{line} ")]


def copy_file(note_path, repo, repo_path, site_path):
    """Copy path from note_path to site_path.
    - Copy .MD files to _posts_path with YAML front matter, adjusted links, and
      slugified path if note_path younger post_path.
    - Copy other valid files with slugified filename (only) following directory
      pattern in note_path. (Assumes asset directories are already slugified)"""
    assert os.path.isfile(note_path), f"{note_path} does not exist"
    # No st_birthtime on Window$; st_ctime is metadata change on others.
    has_birthtime = hasattr(os.stat(note_path), 'st_birthtime')
    note_stat = \
        os.stat(note_path) if has_birthtime else pathlib.Path(note_path).stat()
    date = datetime.date.fromtimestamp(
        note_stat.st_birthtime if has_birthtime else note_stat.st_ctime)
    rel_note_path = note_path.replace(f"{repo_path}/", '')
    note_filename = rel_note_path.split(os.sep)[-1]

    # Process and copy newer .MD files.
    if rel_note_path.endswith('.md'):
        # Process and copy newer .MD file.
        title = note_filename   # if no initial header1 for title
        categories = [slugify(c, True)
            for c in rel_note_path.split(os.sep)[: -1]]
        _posts_path = os.path.join(site_path, '_posts')  # must match prepare
        post_dirname = os.path.join(*[_posts_path, ] + categories)
        post_filename = f"{date}-{slugify(note_filename)}"
        post_path = os.path.join(post_dirname, post_filename)

        # Check modification dates.
        note_changed = not os.path.isfile(post_path) \
            or note_stat.st_mtime > pathlib.Path(post_path).stat().st_mtime
        # logger.debug((note_stat.st_mtime, pathlib.Path(post_path).stat().st_mtime))
        if note_changed:
            lines, tags = list(), list()
            toc, regex = 0, re.compile(r'^[#]{1,6}\s')

            # Read list of lines, reformatting links, parsing tags, finding toc
            # headers, parsing title, and appending comment.
            with open(note_path, encoding='latin1') as rf:
                for line in rf.readlines():
                    lines.append(reformat_links(line.rstrip(), repo))
                    tags += parse_tags(line)
                    toc += 1 if regex.search(line) else 0
            for i, line in enumerate(lines):
                if not line: continue       # skip leading blank lines
                if line.startswith('# '):   # extract title from first heading1
                    title = line[2:].strip()
                    del lines[i]
                    toc -= 1
                    break
            lines.append(f"\n<!-- Modified {time.strftime('%Y-%m-%d:%H:%M:%S')} -->\n")

            # Create list of YAML front matter.
            yaml = format_yaml(title, repo, categories, tags, toc, note_path)

            # Create directory and write post.
            os.makedirs(post_dirname, exist_ok=True)
            logger.info(f"{note_path} \u2192 {post_path}")
            with open(post_path, "w") as wf:
                wf.write('\n'.join(yaml))
                wf.write('\n'.join(lines).lstrip())
        else:
            logger.info(f"UNCHANGED: {note_path}")
    else:
        # Process and copy newer non-.MD files.
        note_dirname = os.path.dirname(rel_note_path)
        asset_dirname = os.path.join(site_path, note_dirname)
        asset_path = os.path.join(asset_dirname, slugify(note_filename))
        # Check modification dates.
        note_changed = not os.path.isfile(asset_path) \
            or note_stat.st_mtime > pathlib.Path(asset_path).stat().st_mtime
        # logger.debug((note_stat.st_mtime, pathlib.Path(post_path).stat().st_mtime))
        if note_changed:
            # TODO: files deleted from note_dir are not removed from asset_dir
            # Create directory and copy asset.
            os.makedirs(asset_dirname, exist_ok=True)
            logger.info(f"{note_path} \u2192 {asset_path}")
            shutil.copy(note_path, asset_path)
        else:
            logger.info(f"UNCHANGED: {note_path}")


def prepare(REPODIR, POSTDIR, REBUILD=False):
    """Copy and modify valid paths from REPODIR to POSTDIR. If REBUILD, remove
    _posts and _site directories."""
    repo_path = os.path.realpath(REPODIR)
    logger.debug(f"repo_path: {repo_path}")
    repo = os.path.normpath(repo_path).split(os.sep)[-1]
    logger.debug(f"repo: {repo}")
    site_path = os.path.realpath(POSTDIR)
    logger.debug(f"site_path: {site_path}")

    assert os.path.isdir(repo_path), f"{repo_path} is not a directory"
    assert os.path.isdir(site_path), f"{site_path} is not a directory"

    # If REBUILD, clean _posts directory.
    _posts_path = os.path.join(site_path, '_posts') # must match copy_file
    if REBUILD and os.path.isdir(_posts_path):
        logger.debug(f"removing: {_posts_path}")
        shutil.rmtree(_posts_path, ignore_errors=True)
    # If REBUILD, clean _site directory. Jekyll should automatically handle.
    _site_path = os.path.join(site_path, '_site')
    if REBUILD and os.path.isdir(_site_path):
        logger.debug(f"removing: {_site_path}")
        shutil.rmtree(_site_path, ignore_errors=True)

    # Collect paths to modify and copy.
    paths = valid_paths(repo_path)
    for path in sorted(paths):
        copy_file(path, repo, repo_path, site_path)


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
            ['template.py', '..', '../docs/', ],
            # ['template.py', '-?', ],
        ]
        # slugify test
        #value = '/obsidian/NestedFolder/Foo & Bar/2024-03-21-Test%20with__spaces, éh? !@%_.md'
        #logger.info((value, slugify(value, True),))
        for test in tests:
            logger.debug(f"# {' '.join(test)}")
            main(test)
    else:
        main(sys.argv)
