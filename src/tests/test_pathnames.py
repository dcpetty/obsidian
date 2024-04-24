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
import os, shutil, unittest

from obsidianjekyll.paths import *
from obsidianjekyll.pathnames import *
from __main__ import log

# Set up logging.
logger = log(__name__, 'tests')


class TestPathNames(unittest.TestCase):
    """Test obsidianjekyll.pathnames."""


    def setUp(self):
        """Setup pathnames for testing"""
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        self.remove = os.path.realpath(os.path.join('.', REMOVE))
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
        logger.info(f"{repr(self.pathnames.paths)}")
        pass


    def test_path_names(self):
        """Test pathnames.path_names."""
        logger.info(f"{repr(self.pathnames.path_names)}")
        pass
