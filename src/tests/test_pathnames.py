#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_pathnames.py
#
# https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
#
"""
test_pathnames.py tests obsidianjekyll.pathnames.
"""

import inspect, os, shutil, tempfile, unittest

from . import paths, pathnames, log
Paths = paths.Paths
PathNames = pathnames.PathNames

# Set up logging.
logger = log.log(__name__, 'tests')


class TestPathNames(unittest.TestCase):
    """Test obsidianjekyll.pathnames."""


    def setUp(self):
        """Setup pathnames for testing"""
        """
        import logging
        loggers = [logging.getLogger(name)
            for name in logging.root.manager.loggerDict]
        for l in loggers:
            l.setLevel('DEBUG')
        """
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        tmp = os.path.realpath(tempfile.mkdtemp())  # tempfile make be a link
        self.remove = os.path.join(tmp, REMOVE)
        self.repo = 'pathnames'
        self.repodir = os.path.join(self.remove, self.repo)
        self.sitedir = os.path.join(self.repodir, 'docs')
        os.makedirs(self.sitedir, exist_ok=True)
        self.paths = Paths(repodir=self.repodir, postdir=self.sitedir)
        pass


    def tearDown(self):
        """Clean up pathnames and any added directories."""
        logger.debug(f"Removing '{self.remove}'\u2026")
        shutil.rmtree(self.remove)
        pass


    def test_paths(self):
        """Test pathnames.paths. Similar to tests in test_paths."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        logger.info(f" repo_path: {repr(self.repodir)} \u2192 {repr(self.paths.repo_path)}")
        self.assertEqual(self.repodir, self.paths.repo_path)
        logger.info(f"      repo: {repr(self.repo)} \u2192 {repr(self.paths.repo)}")
        self.assertEqual(self.repo, self.paths.repo)
        logger.info(f" site_path: {repr(self.sitedir)} \u2192 {repr(self.paths.site_path)}")
        self.assertEqual(self.sitedir, self.paths.site_path)
        postsdir = os.path.join(self.sitedir, '_posts')
        logger.info(f"posts_path: {repr(postsdir)} \u2192 {repr(self.paths.posts_path)}")
        self.assertEqual(postsdir, self.paths.posts_path)
        pass


    def test_path_names(self):
        """Test pathnames.path_names."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        # Touch files in lists.
        mds = [
            'file1.md',
            'foo/file2.md',
            'foo/bar/file3.md',
            'foo/bar/baz/file4.md',
        ]
        pngs = [
            'file1.png',
            'foo/file2.png',
            'foo/bar/file3.png',
            'foo/bar/baz/file4.png',
        ]
        jpgs = [
            'file1.jpg',
            'foo/file2.jpg',
            'foo/bar/file3.jpg',
            'foo/bar/baz/file4.jpg',
        ]
        htmls = [
            'file1.html',
            'foo/file2.html',
            'foo/bar/file3.html',
            'foo/bar/baz/file4.html',
        ]
        others = [
            'README.md',
            '.gitignore',
            '.git/TEST',
            'src/src.md',
            'src/src.file',
            'docs/docs.md',
            'docs/docs.file',
        ]
        for name in mds + pngs + jpgs + htmls + others:
            pathname = os.path.join(self.repodir, name)
            dirname, filename = os.path.split(pathname)
            logger.debug(f"Creating {dirname}/{filename}")
            os.makedirs(dirname, exist_ok=True)
            with open (pathname, 'a'): pass
        # Check pathnames property for various scenarios.
        for expected, inc, exc in [
            # Expected Obsidian uses.
            (mds + pngs + jpgs + htmls, None, None, ),
            # Only one included glob, expected excluded glob.
            (mds, ['*.md', ], None, ),
            # Only one included glob, no excluded globs.
            ([f for f in mds + others if f.endswith('md')], ['*.md', ], [],),
            # Only one included glob, '**/foo/**/baz' excluded.
            ([f for f in mds + pngs + jpgs + htmls + others
                if f.endswith('md') and not f.startswith('foo/bar/baz')],
                    ['*.md', ], ['**/foo/**/baz/*.md'],),
            # No included globs, expected excluded glob.
            ([], [], None),
            # No included globs, no excluded globs.
            ([], [], None),
        ]:
            sorted_expected = sorted(expected)
            pathnames = PathNames(self.paths, to_inc=inc, to_exc=exc)
            sorted_actual = sorted([name.replace(f"{self.paths.repo_path}/", '')
                for name in pathnames.path_names])
            logger.info(f"path_names: {sorted_expected} \u2192 {sorted_actual}")
            logger.debug(
                    f"path_names:"
                f"\n{'\n'.join(['\'' + s + '\'' for s in sorted_expected])}"
                f"\n\u2192\n"
                f"{'\n'.join(['\'' + s + '\'' for s in sorted_actual])}")
            self.assertEqual(sorted_actual, sorted_expected)
        pass
