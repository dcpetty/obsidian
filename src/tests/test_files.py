#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_files.py
#
# https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
#
"""
test_files.py tests obsidianjekyll.files.
"""
# TODO: complete test cases

import inspect, os, shutil, tempfile, unittest

from . import paths, pathnames, files, log
Paths = paths.Paths
PathNames = pathnames.PathNames
Files = files.Files

# Set up logging.
logger = log.log(__name__, 'tests')


class TestFiles(unittest.TestCase):
    """Test obsidianjekyll.pathnames."""


    def setUp(self):
        """Setup pathnames for testing"""
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        tmp = os.path.realpath(tempfile.mkdtemp())  # tempfile make be a link
        self.remove = os.path.join(tmp, REMOVE)
        self.repo = 'pathnames'
        self.repodir = os.path.join(self.remove, self.repo)
        self.sitedir = os.path.join(self.repodir, 'docs')
        os.makedirs(self.sitedir, exist_ok=True)
        self.paths = Paths(repodir=self.repodir, postdir=self.sitedir)
        self.pathnames = PathNames(self.paths)  # TODO: self.repodir is empty
        self.files = Files(self.pathnames)
        pass


    def tearDown(self):
        """Clean up pathnames and any added directories."""
        logger.debug(f"Removing '{self.remove}'\u2026")
        shutil.rmtree(self.remove)
        pass


    def test_paths(self):
        """Test pathnames.paths."""

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

        # TODO: complete test case
        logger.info(f"{repr(self.files.path_names)}")
        pass


    def test_files(self):
        """Test pathnames.files."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        # TODO: complete test case
        logger.info(f"{repr(self.files.files)}")
        pass
