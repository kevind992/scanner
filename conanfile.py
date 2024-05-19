from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.system.package_manager import Apt

class Scanner(ConanFile):
    name = "scanner"
    generators = ("CMakeToolchain", "CMakeDeps")
    settings = ("os", "build_type", "arch", "compiler")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
    
    def layout(self):
        cmake_layout(self)

    def package(self):
        cmake = CMake(self)
        cmake.install()
