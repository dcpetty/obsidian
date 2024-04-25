#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __main__.py
#
"""
__main__.py sets dunder variables and imports and copies a REPODIR Obsidian
repository to a POSTDIR Jekyll repository, modifying the pathnames appropriately.
"""

__version__ = "0.0.4"

__all__ = ["log", "log_path", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

from sys import path
from pathlib import Path
from collections import OrderedDict
# Add package directory to path.
path.insert(1, str(Path(__file__).resolve().parents[0]))
path = list(OrderedDict.fromkeys(path))

import argparse, logging, os, shutil, sys
from cli import Parser
from paths import Paths
from pathnames import PathNames
from files import Files
from log import log, log_path

# Set up logging.
logger = log(__name__, 'obsidian')


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
    files.copy_files()              # copy changed files from Obsidian to Jekyll


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
        loggers = [logging.getLogger(name)
            for name in logging.root.manager.loggerDict]
        for l in loggers:
            l.setLevel('DEBUG')
    if pa.REPODIR:
        logger.debug(f"REPODIR = {repr(pa.REPODIR)}")
    if pa.POSTDIR:
        logger.debug(f"POSTDIR = {repr(pa.POSTDIR)}")
    logger.debug(f"VERBOSE \u2192 {repr(log_path())}")
    if pa.REBUILD:
        logger.debug(f"REBUILD Jekyll site...")

    prepare(pa.REPODIR, pa.POSTDIR, pa.REBUILD)


if __name__ == '__main__':
    # Check whether imported in an IDE.
    is_idle, is_pycharm, is_jupyter = (
        'idlelib' in sys.modules,
        int(os.getenv('PYCHARM', 0)),
        '__file__' not in globals()
    )
    if any((is_idle, is_pycharm, is_jupyter,)):
        logger.debug(f"logpath: {log_path()}")
        tests = [
            ['obsidianjekyll.py', '..', '../docs/', ],
            # ['obsidianjekyll.py', '-?', ],
        ]
        for test in tests:
            logger.debug(f"# {' '.join(test)}")
            main(test)
    else:
        main(sys.argv)
