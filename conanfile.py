from conans import ConanFile, tools
import os


class KainjowmustacheConan(ConanFile):
    name = "Kainjow_Mustache"
    version = "2.0"
    license = "Boost Software License - Version 1.0"
    # No settings/options are necessary, this is header only
    build_policy="missing" # header only no need to build it

    def source(self):
        self.run("git clone --branch v2.0 --depth 1 https://github.com/kainjow/Mustache")

    def package(self):
        self.copy("mustache.hpp", dst="include/kainjow", src="Mustache")

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths

