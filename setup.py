VERSION_MAJOR = 0
VERSION_MINOR = 0
VERSION_PATCH = 1
VERSION_STRING = '%s.%s.%s' % (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
__version__ = VERSION_STRING

from setuptools import Extension, setup, find_namespace_packages
from Cython.Build import cythonize
import sys
import glob
import numpy as np

if sys.version_info[0] == 2:
    raise Exception('Python 2.x is no longer supported')

with open("README.md", 'r') as f:
    long_description = f.read()

ext_gomea = Extension("gomea",
        glob.glob("src/gomea/cython/*.pyx") +
        glob.glob("src/common/cpp/*.cpp") + glob.glob("src/utils/cpp/*.cpp") + glob.glob("src/fitness/cpp/*.cpp"),
        include_dirs=["include/","src/"],
        language="c++",
        extra_compile_args=["-std=c++17"],
        extra_link_args=["-std=c++17"])

ext_discrete = Extension("DiscreteGOMEA",
        glob.glob("src/discrete_gomea/cython/*.pyx") + glob.glob("src/discrete_gomea/cpp/*.cpp") +
        glob.glob("src/common/cpp/*.cpp") + glob.glob("src/utils/cpp/*.cpp") + glob.glob("src/fitness/cpp/*.cpp"),
        include_dirs=["include/","src/"],
        language="c++",
        extra_compile_args=["-std=c++17"],
        extra_link_args=["-std=c++17"])

ext_real_valued = Extension("RealValuedGOMEA",
        glob.glob("src/real_valued_gomea/cython/*.pyx") + glob.glob("src/real_valued_gomea/cpp/*.cpp") +
        glob.glob("src/common/cpp/*.cpp") + glob.glob("src/utils/cpp/*.cpp") + glob.glob("src/fitness/cpp/*.cpp"),
        include_dirs=["include/","src/"],
        language="c++",
        extra_compile_args=["-std=c++17"],
        extra_link_args=["-std=c++17"],
        libraries=["armadillo"],
        library_dirs=[],
        extra_objects=[])

ext_fitness = Extension("Fitness",
        glob.glob("src/fitness/cython/*.pyx") + glob.glob("src/fitness/cpp/*.cpp") +
        glob.glob("src/utils/cpp/*.cpp") + glob.glob("src/common/cpp/*.cpp"),
        include_dirs=["include/","src/"],
        language="c++",
        extra_compile_args=["-std=c++17"],
        extra_link_args=["-std=c++17"])

extensions = [ext_gomea,ext_discrete,ext_real_valued,ext_fitness]

setup(
    name = "gomea",
    description = 'Library for the use of various variants of the Gene-pool Optimal Mixing Evolutionary Algorith (GOMEA).',
    author = 'Anton Bouter',
    author_email = 'Anton.Bouter@cwi.nl',
    url = '',
    version = __version__,
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    ext_modules = cythonize(extensions,
        include_path = glob.glob("src/*/cython/") + [np.get_include()],
        gdb_debug = False,
        language_level = "3"),
    zip_safe = False
    #packages=['fitness'],
    #package_data={'fitness': ['src/fitness/cython/Fitness.pxd']},
)

