from conans import ConanFile


class KainjowmustacheConan(ConanFile):
    name = "kainjow-mustache"
    version = "3.1"
    license = "Boost Software License - Version 1.0"
    url = "https://github.com/inexorgame/conan-kainjow-mustache"
    description = "Mustache text templates for modern C++"
    # No settings/options are necessary, this is header only
    build_policy = "missing" # header only no need to build it

    def source(self):
        self.run("git clone --branch v%s --depth 1 https://github.com/kainjow/Mustache" % (self.version))

    def package(self):
        self.copy("mustache.hpp", dst="include/kainjow", src="Mustache")

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
