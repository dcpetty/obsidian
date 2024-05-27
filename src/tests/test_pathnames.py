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
import inspect, os, shutil, unittest

from . import paths, pathnames, log
Paths = paths.Paths
PathNames = pathnames.PathNames

# Set up logging.
logger = log.log(__name__, 'tests')


class TestPathNames(unittest.TestCase):
    """Test obsidianjekyll.pathnames."""


    def setUp(self):
        """Setup pathnames for testing"""
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        dot = os.path.dirname(os.path.realpath(__file__))
        self.remove = os.path.join(dot, REMOVE)
        self.repo = 'pathnames'
        self.repodir = os.path.join(self.remove, self.repo)
        self.postdir = os.path.join(self.repodir, 'docs')
        os.makedirs(self.postdir, exist_ok=True)
        self.paths = Paths(repodir=self.repodir, postdir=self.postdir)
        self.pathnames = PathNames(self.paths)
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
        logger.info(f"{repr(self.pathnames.paths)}")
        pass


    def test_path_names(self):
        """Test pathnames.path_names."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        # TODO: complete test case
        logger.info(f"{repr(self.pathnames.path_names)}")
        pass
