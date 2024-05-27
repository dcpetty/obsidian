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
# TODO: complete test cases

import inspect, os, shutil, unittest

from . import paths, log
Paths = paths.Paths

# Set up logging.
logger = log.log(__name__, 'tests')


class TestPaths(unittest.TestCase):
    """Test obsidianjekyll.paths."""


    def setUp(self):
        """Setup Paths for testing"""
        REMOVE = 'REMOVE'   # self.remove will be removed, so name carefully!
        dot = os.path.dirname(os.path.realpath(__file__))
        self.remove = os.path.join(dot, REMOVE)
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

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        logger.info(f"{repr(self.repo)} \u2192 {repr(self.paths.repo)}")
        self.assertEqual(self.repo, self.paths.repo)
        pass


    def test_repodir(self):
        """Test paths.repodir."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        relrepodir, relrepo_path = \
            os.path.relpath(self.repodir), os.path.relpath(self.paths.repo_path)
        logger.info(f"{repr(relrepodir)} \u2192 {repr(relrepo_path)}")
        self.assertEqual(self.repodir, self.paths.repo_path)
        pass


    def test_sitedir(self):
        """Test paths.sitedir."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        relsitedir, relsite_path = \
            os.path.relpath(self.postdir), os.path.relpath(self.paths.site_path)
        logger.info(f"{repr(relsitedir)} \u2192 {repr(relsite_path)}")
        self.assertEqual(self.repodir, self.paths.repo_path)
        pass


    def test_postsdir(self):
        """Test paths.repo."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        postsdir = os.path.join(self.postdir, '_posts')
        relpostsdir, relposts_path = \
            os.path.relpath(postsdir), os.path.relpath(self.paths.posts_path)
        logger.info(f"{repr(relpostsdir)} \u2192 {repr(relposts_path)}")
        self.assertEqual(postsdir, self.paths.posts_path)
        pass


    def test_slugify(self):
        """Test paths.slugify()."""

        # Log test_name.
        test_name = inspect.currentframe().f_code.co_name
        logger.info(f"In {test_name}()\u2026")

        prefix = '/foo/bar/baz' # already slugified and lower case
        sources = [
            'This is a test file.txt',
            'This%20is-a%20test_file.py',
            '¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫˜µ≤≥÷.png',
            'CamenCaseFilename.MD',
        ]
        values = [
            'This-is-a-test-file.txt',
            'This-is-a-test-file.py',
            'TMao-a-c.png',
            'CamenCaseFilename.MD',
        ]
        # Test slugify with (default) preserve_case=False.
        for i, p in enumerate([os.path.join(prefix, f) for f in sources]):
            sp = self.paths.slugify(p)
            vp = os.path.join(prefix, values[i]).lower()
            logger.info(f"{p} \u2192 {sp} \u225f {vp}")
            self.assertEqual(vp, sp)
        # Test slugify with preserve_case=True
        for i, p in enumerate([os.path.join(prefix, f) for f in sources]):
            sp = self.paths.slugify(p, True)
            vp = os.path.join(prefix, values[i])
            logger.info(f"{p} \u2192 {sp} \u225f {vp}")
            self.assertEqual(vp, sp)
        pass
