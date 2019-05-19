from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Compiler.Options import get_directive_defaults

get_directive_defaults()['linetrace'] = True
get_directive_defaults()['binding'] = True

extensions = [
    Extension("randgen", ["randgen.pyx"]),
    Extension("linalg", ["linalg.pyx"],define_macros=[('CYTHON_TRACE', '1')]),
]
setup(
 name='test',
 ext_modules = cythonize(extensions,compiler_directives = {'language_level': 3}),

 )
