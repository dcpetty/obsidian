#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_paths.py
#
# https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
#
"""
test_paths.py tests obsidianjekyll.paths.
"""
import os, shutil, unittest

from obsidianjekyll.paths import *
from __main__ import log

# Set up logging.
logger = log(__name__, 'tests')


class TestPaths(unittest.TestCase):
    """Test obsidianjekyll.paths."""


    def setUp(self):
        """Setup Paths for testing"""
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        self.remove = os.path.realpath(os.path.join('.', REMOVE))
        self.repo = 'paths'
        self.repodir = os.path.join(self.remove, self.repo)
        self.postdir = os.path.join(self.repodir, 'docs')
        os.makedirs(self.postdir, exist_ok=True)
        self.paths = Paths(repodir=self.repodir, postdir=self.postdir)
        pass


    def tearDown(self):
        """Clean up Paths and any added directories."""
        shutil.rmtree(self.remove)
        pass


    def test_repo(self):
        """Test paths.repo."""
        logger.info(f"{repr(self.repo)} \u2192 {repr(self.paths.repo)}")
        self.assertEqual(self.repo, self.paths.repo)
        pass


    def test_repodir(self):
        """Test paths.repodir."""
        relrepodir, relrepo_path = \
            os.path.relpath(self.repodir), os.path.relpath(self.paths.repo_path)
        logger.info(f"{repr(relrepodir)} \u2192 {repr(relrepo_path)}")
        self.assertEqual(self.repodir, self.paths.repo_path)
        pass


    def test_sitedir(self):
        """Test paths.sitedir."""
        relsitedir, relsite_path = \
            os.path.relpath(self.postdir), os.path.relpath(self.paths.site_path)
        logger.info(f"{repr(relsitedir)} \u2192 {repr(relsite_path)}")
        self.assertEqual(self.repodir, self.paths.repo_path)
        pass


    def test_postsdir(self):
        """Test paths.repo."""
        postsdir = os.path.join(self.postdir, '_posts')
        relpostsdir, relposts_path = \
            os.path.relpath(postsdir), os.path.relpath(self.paths.posts_path)
        logger.info(f"{repr(relpostsdir)} \u2192 {repr(relposts_path)}")
        self.assertEqual(postsdir, self.paths.posts_path)
        pass
