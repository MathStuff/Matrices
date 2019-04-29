from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension("randgen", ["randgen.pyx"]),
    Extension("linalg", ["linalg.pyx"]),
]
setup(
 name='test',
 ext_modules = cythonize(extensions)
 )
