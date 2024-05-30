#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __main__.py
#
"""
__main__.py import run_tests and runs it.
"""
# From https://stackoverflow.com/a/65780624/17467335 to fix relative imports.
from sys import path as _p
from pathlib import Path as _P
from collections import OrderedDict as _OD
# path hack: add package directory to path.
_p.insert(1, str(_P(__file__).resolve().parents[1]))
_p = list(_OD.fromkeys(_p))

# import test modules.
from tests import test_runner
run_tests = test_runner.run_tests

if __name__ == '__main__':
    run_tests()