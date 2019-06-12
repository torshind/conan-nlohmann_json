from conans import ConanFile, CMake


class NlohmannJsonConan(ConanFile):
    name = "nlohmann_json"
    version = "3.6.1"
    license = "MIT"
    homepage = "https://nlohmann.github.io/json/"
    url = "https://github.com/torshind/conan-nlohmann_json/"
    description = "JSON for Modern C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "*"

    def source(self):
        self.run("git clone --branch v"
                 + self.version
                 + " https://github.com/nlohmann/json.git")

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["JSON_BuildTests"] = "OFF"
        cmake.definitions["JSON_MultipleHeaders"] = "ON"
        cmake.configure(source_folder="json")
        cmake.install()

    def package_info(self):
        self.info.header_only()
