from conans import ConanFile, CMake, tools


class NlohmannJsonConan(ConanFile):
    name = "nlohmann_json"
    version = "3.6.1"
    license = "MIT"
    url = "https://nlohmann.github.io/json/"
    description = "JSON for Modern C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/nlohmann/json.git", "v" + self.version)

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["JSON_BuildTests"] = "OFF"
        cmake.definitions["JSON_MultipleHeaders"] = "ON"
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.info.header_only()
