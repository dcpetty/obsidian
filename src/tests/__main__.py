#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __main__.py
#
"""
__main__.py imports test_runner.run_tests and runs it.
"""

__version__ = "0.0.1"

__all__ = ['log', 'log_path', ]

from sys import path
from pathlib import Path
from collections import OrderedDict
# Add package directory to path.
path.insert(1, str(Path(__file__).resolve().parents[1]))
# Add obsidianjekyll to path so its imports still work.
path.insert(1, str(Path(__file__).resolve().parents[1] / 'obsidianjekyll'))
path = list(OrderedDict.fromkeys(path))

from obsidianjekyll.log import log, log_path

# Set up logging.
logger = log(__name__, 'tests')

# Run test suite in run_tests.
from tests.test_runner import run_tests
run_tests()
