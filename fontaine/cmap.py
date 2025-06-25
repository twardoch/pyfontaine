#
# cmap.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.
from importlib import import_module

import fontaine.charsets.internals
import fontaine.ext
from fontaine.ext.base import PackageRequiredException


class Library:
    def __init__(self, collections=["all"]):
        self._charsets = []
        self.collections = collections

    def register(self, charset):
        charset_ = charset()
        if not getattr(charset_, "short_name", False):
            setattr(charset_, "short_name", charset.__module__.split(".")[-1])
        self._charsets.append(charset_)

    @property
    def charsets(self):
        if self._charsets:
            return self._charsets

        for ext in fontaine.ext.__all__:
            try:
                module = import_module("fontaine.ext.%s" % ext)
                extension_name = module.Extension.extension_name
            except (ImportError, AttributeError):
                continue
            except PackageRequiredException as ex:
                import sys

                sys.stderr.write("WARNING: %s\n" % ex.message)
                continue

            if "all" in self.collections or extension_name in self.collections:
                for charset_klass in module.Extension.get_charsets():
                    self.register(charset_klass)

        if "all" in self.collections or "pyfontaine" in self.collections:
            for ext in fontaine.charsets.internals.__all__:
                module = import_module("fontaine.charsets.internals.%s" % ext)
                self.register(module.Charset)
        return self._charsets


library = Library()
