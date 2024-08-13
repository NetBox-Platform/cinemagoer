# Copyright 2009 H. Turgut Uyar <uyar@tekir.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
This package provides scripts and files for internationalization of Cinemagoer.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import gettext
import os

LOCALE_DIR = os.path.dirname(__file__)
def dummy_translation(domain, localedir=None, languages=None, class_=None, fallback=False, codeset=None):
    return gettext.NullTranslations()

gettext.translation = dummy_translation

translation = gettext.translation('imdbpy', LOCALE_DIR)
_ = translation.gettext
