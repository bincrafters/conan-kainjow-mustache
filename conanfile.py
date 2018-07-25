from conans import ConanFile, tools
import os


class KainjowmustacheConan(ConanFile):
    name = "kainjow-mustache"
    version = "3.1"
    license = "Boost Software License - Version 1.0"
    url = "https://github.com/inexorgame/conan-kainjow-mustache"
    homepage = "https://github.com/kainjow/Mustache"
    description = "Mustache text templates for modern C++"
    # No settings/options are necessary, this is header only
    no_copy_source = True

    source_subfolder = "Mustache"

    def source(self):
        archive_url = "https://github.com/kainjow/Mustache/archive/v{!s}.zip".format(self.version)
        tools.get(archive_url, sha256="f327d3b9c7313f7efcb1209f44fb10a5e65da27d28bbdc4e0518443c3add0dc5")
        os.rename("Mustache-{!s}".format(self.version), self.source_subfolder)

    def package(self):
        self.copy("mustache.hpp", dst="include/kainjow", src=self.source_subfolder)

    def package_id(self):
        self.info.header_only()
