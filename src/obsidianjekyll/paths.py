#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# paths.py
#
"""
paths.py defines Paths class with repo_path, repo, site_path, and posts_path
properties and slugify function.
"""
import os, re, unicodedata
from .log import log

__all__ = ["Paths", ]
__author__ = "David C. Petty"
__copyright__ = "Copyright 2024, David C. Petty"
__credits__ = ["David C. Petty", ]
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__maintainer__ = "David C. Petty"
__email__ = "dcp@acm.org"
__status__ = "Development"

# Set up logging.
logger = log(__name__, 'obsidian')


class Paths(object):
    """Keep track of the directories, paths, and repository."""

    _default_repodir = '.'
    _default_postdir = './docs'


    def __init__(self, repodir=None, postdir=None):
        """Initialize paths for repository and site."""

        self._repodir = repodir if repodir else type(self)._default_repodir
        self._postdir = postdir if postdir else type(self)._default_postdir
        self._repo_path = os.path.realpath(self._repodir)   # no trailing '/'
        self._repo = os.path.normpath(self._repo_path).split(os.sep)[-1]
        self._site_path = os.path.realpath(self._postdir)   # no trailing '/'
        self._posts_path = os.path.join(self.site_path, '_posts')

        assert os.path.isdir(self._repo_path), \
            f"'{self._repo_path}' is not a directory"
        assert os.path.isdir(self._site_path), \
            f"'{self._site_path}' is not a directory"
        # _site_path must exist; _posts_path (which must be a dir) may not.
        assert not os.path.exists(self._posts_path) \
            or os.path.isdir(self._posts_path), \
            f"'{self._posts_path}' is not a directory"

        self._log()


    def _log(self):
        logger.debug(f"repo_path:  {self.repo_path}")
        logger.debug(f"repo:       {self.repo}")
        logger.debug(f"site_path:  {self.site_path}")
        logger.debug(f"posts_path: {self.posts_path}")
        #logger.info(f"perma: {self.permalink(os.path.join(self.repo_path, 'TestPages/This is a note with spaces,_ éh? !@$-.md'))}")
        #logger.info(f"post:  {self.post_path(os.path.join(self.repo_path, 'TestPages/This is a note with spaces,_ éh? !@$-.md'), '2024-03-22')}")
        #logger.info(f"asset: {self.asset_path(os.path.join(self.repo_path, 'assets/obsidian/Pasted image 20240326090137.png'))}")


    # Properties repo_path, repo, site_path, posts_path.
    def _get_repo_path(self): return self._repo_path
    repo_path = property(_get_repo_path)
    def _get_repo(self): return self._repo
    repo = property(_get_repo)
    def _get_site_path(self): return self._site_path
    site_path = property(_get_site_path)
    def _get_posts_path(self): return self._posts_path
    posts_path = property(_get_posts_path)


    # Utilities for note_path.
    def _check_dir(self, d): assert os.path.isdir(d), f"'{d}' is not a directory"; return d
    def _check_file(self, f): assert os.path.isfile(f), f"'{f}' is not a file"; return f
    def note_dirname(self, note_path): return self._check_dir(os.path.dirname(note_path))
    def note_filename(self, note_path): return os.path.basename(self._check_file(note_path))
    def rel_note_path(self, note_path): return self._check_file(note_path).replace(f"{self.repo_path}/", '')
    def rel_note_dirname(self, note_path): return os.path.dirname(self.rel_note_path(note_path))
    def permalink(self, note_path): return f"/{os.path.splitext(self.slugify(self.rel_note_path(note_path)))[0]}/"
    def post_path(self, note_path, yaml_date): return os.path.join(self.posts_path,
        f"{yaml_date}-{self.slugify(self.note_filename(note_path))}")
    def asset_path(self, note_path): return os.path.join(self.site_path,
        self.rel_note_dirname(note_path), self.slugify(self.note_filename(note_path)))


    @staticmethod
    def slugify(path, preserve_case=False):
        """Return simple slugified path. Used to slugify paths and links. If
        preserve_case is False, convert slugified path to lowercase.
        - split off any extension and work with root
        - replace '%20' with ' '
        - unicodedata.normalize 'NFKD' to 'ascii'
        - remove everything *not* letters, numerals, or '/._-'
        - replace ' ' or '.' or '_' with '-' (Jekyll)
        - remove duplicate '-'s (Jekyll)
        - add back on the extension
        """

        # https://stackoverflow.com/a/27264385
        root, ext = os.path.splitext(path)
        slugified = re.sub('[-]{2,}', '-',
            re.sub(r'[\s._]', '-', re.sub(r'[^/\w\s._-]', '',
                unicodedata.normalize('NFKD', re.sub(r'%20', ' ', root))
                    .encode('ascii', 'ignore').decode('ascii')))) \
                        .strip('-') + ext
        return slugified if preserve_case else slugified.lower()
