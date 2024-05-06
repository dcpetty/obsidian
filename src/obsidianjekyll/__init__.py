#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# __init__.py
#
"""
__init__.py imports modules and sets dunder variables.
"""
from . import cli, paths, pathnames, files, log

__version__ = "0.0.4"

__all__ = ["cli", "paths", "pathnames", "files", "log",
           "__version__", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

# Set up logging.
logger = log.log(__name__, 'obsidian')
