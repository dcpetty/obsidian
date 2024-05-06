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

import inspect, os, shutil, unittest

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
        self.remove = os.path.realpath(os.path.join('.', REMOVE))
        self.repo = 'files'
        self.repodir = os.path.join(self.remove, self.repo)
        self.postdir = os.path.join(self.repodir, 'docs')
        os.makedirs(self.postdir, exist_ok=True)
        self.paths = Paths(repodir=self.repodir, postdir=self.postdir)
        self.pathnames = PathNames(self.paths)
        self.files = Files(self.pathnames)
        pass


    def tearDown(self):
        """Clean up pathnames and any added directories."""
        shutil.rmtree(self.remove)
        pass


    def test_paths(self):
        """Test pathnames.paths."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        # TODO: complete test case
        logger.info(f"{repr(self.files.paths)}")
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
