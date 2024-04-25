#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_runner.py
#
# https://www.internalpointers.com/post/run-painless-test-suites-python-unittest
#
"""
test_runner.py defines run_tests function.
"""
import unittest
from __main__ import log, log_path

# Set up logging.
logger = log(__name__, 'tests')
logger.info(f"log: {log_path()}")

# import test modules.
from tests import test_paths, test_pathnames, test_files

__all__ = [ 'run_tests', ]


def run_tests(verbosity=2):
    """Run all tests in test_paths."""

    # initialize the test suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(test_paths))
    suite.addTests(loader.loadTestsFromModule(test_pathnames))
    suite.addTests(loader.loadTestsFromModule(test_files))

    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
