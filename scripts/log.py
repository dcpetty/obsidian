#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# log.py
#
import logging, os, tempfile

1234567890123456789012345678901234567890123456789012345678901234567890
"""
Logging module that logs to the console and a temporary log file.
"""

__version__ = "0.0.4"

__all__ = ["log", "log_path", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

path = globals().get('path')    # Initialize global path to temporary log.
fix = lambda prefix: f'{prefix if prefix else "PREFIX"}-'

def log(name, prefix=None, level=logging.INFO):
    """If logger with name exists, return it with updated FileStream with new
    temp log file (if prefix changed) and level, otherwise return new logger with
    name logging to sys.stderr and temp log file with name prefix at level. """
    global path
    new_file = path is None

    # If name already has a logger, return it with updated FileStream with new
    # temp log file (if prefix changed) and level.
    if name in logging.root.manager.loggerDict:
        logger = logging.getLogger(name)
        update_prefix(logger, prefix)
        logger.setLevel(level)
        return logger

    # Initialize basic configuration with name and level.
    logging.basicConfig(filename=os.devnull, level=logging.NOTSET, force=True)
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create file handler which logs messages at level.
    if new_file:
        fd, path = tempfile.mkstemp('.log', fix(prefix))

    fh = logging.StreamHandler(open(path, 'a'))
    fh.setLevel(logging.DEBUG)

    # Create console handler which logs messages at level.
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter and add it to handlers.
    FORMAT = '{asctime:s} {name:^10s} ' \
             '[{threadName:^10s}] {levelname:<8s} {message:s}'
    FORMAT = '{asctime:s} {name:^10s} {levelname:<8s} {message:s}'
    formatter = logging.Formatter(
        FORMAT, style='{', datefmt='%Y/%m/%d-%H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add the handlers to logger.
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def update_prefix(logger, prefix):
    """Update logger FileStream with new temp log file, if prefix changed."""
    global path
    fixed = fix(prefix)
    for handler in logger.handlers:
        dirname, basename = os.path.split(handler.stream.name)
        # If StreamHandler name is '*.log' but with a different prefix,
        # replace stream with new temp file descriptor and close old one.
        if basename.endswith('.log') and not basename.startswith(fixed):
            fd, path = tempfile.mkstemp('.log', fixed)
            handler.setStream(open(path, 'a')).close()


def log_path():
    """Return path for temporary log file, or None if not yet set by log()."""
    global path
    return path


if __name__ == '__main__':
    logger = log(__name__)
    logger.info(log_path())
    logger = log(__name__)
    logger.info(log_path())
    logger = log(__name__, 'new-name', logging.DEBUG)
    logger.info(log_path())
    logger = log(__name__, level=logging.DEBUG)
    logger.info(log_path())
    logger.debug('D: SPAM')
    logging.debug('D: SPAM')
    logger.info('I: SPAM, SPAM')
    logger.warning('W: SPAM, SPAM, SPAM')
    logger.error('E: SPAM, SPAM, SPAM, SPAM')
    logger.critical('C: SPAM, SPAM, SPAM, SPAM, SPAM')

    print(f'\n# logpath: {log_path()}')
    with open(log_path()) as lp:
        for line in lp.readlines():
            print(line.strip())
