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
from . import test_paths, test_pathnames, test_files


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
