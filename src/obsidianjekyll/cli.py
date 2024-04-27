#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# cli.py
#
"""
cli.py defines Parser(argparse.ArgumentParser) class with error function.
"""

__all__ = ["Parser", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

import argparse, sys
from __main__ import __version__
from log import log

# Set up logging.
logger = log(__name__, 'obsidian')


class Parser(argparse.ArgumentParser):
    """Create OptionParser to parse command-line options."""


    def __init__(self, **kargs):
        argparse.ArgumentParser.__init__(self, **kargs)
        # self.remove_argument("-h")
        self.add_argument("-?", "--help", action="help",
                          help="show this help message and exit")
        self.add_argument('--version', action='version',
                          version=f"%(prog)s {__version__}")


    def error(self, msg):
        sys.stderr.write("%s: error: %s\n\n" % (self.prog, msg, ))
        self.print_help()
        sys.exit(2)
