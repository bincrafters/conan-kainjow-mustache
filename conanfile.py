#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, tools
import os


class KainjowmustacheConan(ConanFile):
    name = "kainjow-mustache"
    version = "3.2.1"
    license = "Boost Software License - Version 1.0"
    url = "https://github.com/bincrafters/conan-kainjow-mustache"
    homepage = "https://github.com/kainjow/Mustache"
    author = "Inexor <info@inexor.org>"
    description = "Mustache text templates for modern C++"
    no_copy_source = True
    source_subfolder = "Mustache"

    def source(self):
        archive_url = "https://github.com/kainjow/Mustache/archive/v{!s}.zip".format(self.version)
        tools.get(archive_url, sha256="5c270706928a8e31b84960313a32d0942229fef17a6ab7a6a98abb3c21e55d6f")
        os.rename("Mustache-{!s}".format(self.version), self.source_subfolder)

    def build(self):
        pass

    def package(self):
        self.copy("mustache.hpp", dst="include/kainjow", src=self.source_subfolder)
        self.copy("LICENSE", dst=".", src=self.source_subfolder)

    def package_id(self):
        self.info.header_only()
