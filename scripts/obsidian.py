#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# obsidian.py
#
"""
obsidian.py is...
"""

__version__ = "0.0.1"

__all__ = ["main", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

import argparse, datetime, fnmatch, glob, log, os, pathlib, re, shutil, sys, unicodedata

# Set up logging.
logger = log.log(__name__, 'obsidian')


def valid_paths(repo_path):
    """Return valid paths below repo_paths."""

    # glob all *.* paths below repo_paths.
    all_paths = [ p for p in glob.glob(os.path.join(repo_path, '**/*.*'),
        recursive=True) ]

    # https://stackoverflow.com/a/5141829
    # List of patterns to include.
    to_inc = ['*.md', '*.png', '*.jpg', '*.html', ]
    # List of patterns to exclude.
    to_exc = ['**/.git/**', '**/docs/**', '**/scripts/**', '**/foo/**/bar/*.html']

    # transform glob patterns to regular expressions
    wc_regex = lambda glob: fnmatch.translate(glob.replace('**/', ':GLOB:')) \
        .replace(':GLOB:', '(.*/)*')
    inc_regex = r'|'.join([wc_regex(x) for x in to_inc])
    logger.debug(f"include regex: {inc_regex}")
    exc_regex = r'|'.join([wc_regex(x) for x in to_exc]) or r'$.'
    logger.debug(f"exclude regex: {exc_regex}")

    """
    # Test inc_regex / exc_regex
    test_globs =[
        'foo/bar.md',
        'foo/bar.html',
        '/obsidian/docs/test.md',
        'foo/foo1/bar/blap.md',
        'foo/bar/blap.md',
        'foo/foo1/bar/blap.html',
        'foo/bar/blap.html',
        '/obsidian/foo/foo1/bar/blap.md',
        '/obsidian/foo/bar/blap.md',
        '/obsidian/foo/foo1/bar/blap.html',
        '/obsidian/foo/bar/blap.html',
    ]
    included = {f for f in test_globs if re.match(to_inc, f)}
    logger.debug(f"included: {included}")
    excluded = {f for f in test_globs if not re.match(to_exc, f)}
    logger.debug(f"excluded: {excluded}")
    logger.debug(f"i - e: {included - excluded}")
    logger.debug(f"i & e: {included & excluded}")
    logger.debug(f"i ^ e: {included ^ excluded}")
    """

    included = {p for p in all_paths if re.match(inc_regex, p)}
    logger.debug(f"        included: {included}")
    paths = {p for p in included if not re.match(exc_regex, p)}
    logger.debug(f"and not excluded: {paths}")

    for path in paths:
        logger.debug(f"valid: {path.replace(repo_path + '/', '')}")

    return paths


def slugify(path):
    """Return simple slugified path.
    - split off any extension and work with root
    - replace '%20' with ' '
    - unicodedata.normalize 'NFKD'
    - remove everything *not* letters, numerals, or '/._-'
    - replace ' ' or '.' or '_' with '-' (Jekyll)
    - remove duplicate '-'s (Jekyll)
    - add on the extension
    """
    # https://stackoverflow.com/a/27264385
    root, ext = os.path.splitext(path)
    slugified = re.sub('[-]{2,}', '-',
        re.sub(r'[\s._]', '-', re.sub(r'[^/\w\s._-]', '',
            unicodedata.normalize('NFKD', re.sub(r'%20', ' ', root))
            .encode('ascii', 'ignore').decode('ascii')))) \
                .strip('-').lower() + ext

    return slugified


def format_yaml(repo, path, title, categories, tags):
    """Return YAML front matter for..."""
    logger.debug(f"format_yaml: '{repo}' '{path}' '{title}' '{categories}' '{tags}'")
    categories_yaml = '\n'.join(
        ['categories:'] + [f' - {c}' for c in [repo] + categories]) + '\n' \
            if [repo] + categories else ''
    tags_yaml = '\n'.join(
        ['tags:'] + [f' - {t}' for t in tags]) + '\n' if tags else ''
    yaml = '\n'.join([
        f'---',
        f'title: "{title}"',
        f'{categories_yaml}{tags_yaml}---\n'])

    logger.debug(f"YAML for '{path}'\n{yaml}")

    return yaml


def reformat_links(line, repo, ext):
    """"""
    return line


def parse_tags(line):
    """"""
    return [h.strip()[1:] for h in re.findall('[#]\w+\s', f"{line} ")]


def prepare(REPODIR, POSTDIR):
    """"""
    repo_path = os.path.realpath(REPODIR)
    logger.debug(f"repo_path: {repo_path}")
    repo = os.path.normpath(repo_path).split(os.sep)[-1]
    logger.debug(f"repo: {repo}")
    site_path = os.path.realpath(POSTDIR)
    logger.debug(f"site_path: {site_path}")

    # Clean _posts and _site directories.
    _posts_path = os.path.join(site_path, '_posts')
    if os.path.isdir(_posts_path):
        logger.debug(f"removing: {_posts_path}")
        shutil.rmtree(_posts_path, ignore_errors=True)
    os.mkdir(_posts_path)   # recreate _posts directory
    _site_path = os.path.join(site_path, '_site')
    if os.path.isdir(_site_path):
        logger.debug(f"removing: {_site_path}")
        shutil.rmtree(_site_path, ignore_errors=True)

    # Collect paths to modify and copy.
    paths = valid_paths(repo_path)
    for path in paths:
        date = datetime.date.fromtimestamp(pathlib.Path(path).stat().st_ctime)
        rel_path = path.replace(f"{repo_path}/", '')
        categories = rel_path.split(os.sep)[: -1]
        note_filename = rel_path.split(os.sep)[-1]
        title = note_filename
        if rel_path.endswith('.md'):
            lines, tags = list(), list()
            with open(path, encoding='latin1') as rf:
                for line in rf.readlines():
                    lines.append(line.lstrip())
                    tags += parse_tags(line)
            for i, line in enumerate(lines):
                if not line: continue       # skip leading blank lines
                if line.startswith('# '):   # extract title from first heading1
                    title = line[2: ]
                    lines = lines[i + 1: ]
                    break
            yaml = format_yaml(repo, path, title, categories, tags)
            post_dirname = os.path.join(*[_posts_path, ] + categories)
            post_filename = f"{date}-{slugify(note_filename)}"
            os.makedirs(post_dirname, exist_ok=True)
            post_path = os.path.join(post_dirname, post_filename)
            logger.info(f"{path} \u2192 {post_path}")
            with open(post_path, "w") as wf:
                wf.write(yaml)
                wf.writelines(lines)
        else:
            logger.debug(f"NOT COPIED: '{rel_path}'")


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
        ('-v', '--verbose', 'store_true', 'VERBOSE', False,
         'echo status information', ),
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

    prepare(pa.REPODIR, pa.POSTDIR)


if __name__ == '__main__':
    is_idle, is_pycharm, is_jupyter = (
        'idlelib' in sys.modules,
        int(os.getenv('PYCHARM', 0)),
        '__file__' not in globals()
    )
    if any((is_idle, is_pycharm, is_jupyter,)):
        logger.debug(f"logpath: {log.log_path()}")
        tests = [
            ['template.py', '..', '../docs/', '-v', ],
            ['template.py', '-?', ],
        ]
        value = '/obsidian/NestedFolder/2024-03-21-Test%20with__spaces, éh? !@%_.md'
        logger.info((value, slugify(value),))
        for test in tests:
            logger.debug(f"# {' '.join(test)}")
            main(test)
    else:
        main(sys.argv)
