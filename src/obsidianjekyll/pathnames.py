#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pathnames.py
#
"""
pathnames.py defines PathNames class with paths and path_names properties.
"""

__all__ = ["PathNames", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

import glob, fnmatch, os, re
from log import log

# Set up logging.
logger = log(__name__, 'obsidian')


class PathNames(object):
    """Collect Jekyll file pathnames from an Obsidian vault."""

    # List of patterns to include.
    _default_to_inc = ['*.md', '*.png', '*.jpg', '*.html', ]
    # List of patterns to exclude.
    _default_to_exc = ['**/.git*/**', '**/docs/**', '**/scr/**', '**/README.md',
        '**/foo/**/bar/*.html']  # TODO: this is simply to test valid_paths

    def __init__(self, paths, to_inc=None, to_exc=None):
        """Created sorted list of valid paths below repo_path."""
        self._paths = paths
        self._to_inc = to_inc if to_inc else type(self)._default_to_inc
        self._to_exc = to_exc if to_exc else type(self)._default_to_exc
        self._path_names = self._valid_paths(self.paths.repo_path, self._to_inc, self._to_exc)

        self._log()


    def _log(self):
        # logger.debug(f"paths:       {self.paths}")
        # logger.debug(f"path_names:  {self.path_names}")
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
            logger.debug(f"include regex:    {inc_regex}")
            logger.debug(f"exclude regex:    {exc_regex}")
            logger.debug(f"        included: {included}")
            logger.debug(f"and not excluded: {paths}")
            # Log each valid path to process relative to repo_path.
            for path in paths:
                valid_pathname = path.replace(repo_path + '/', '')
                logger.debug(f"valid:            {valid_pathname}")

        _log_valid_paths()

        return paths
