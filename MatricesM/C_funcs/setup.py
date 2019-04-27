from distutils.core import setup, Extension

module = Extension("fillModule",sources=["fill.c"])

setup(name="fillerPack",version="1.0",description="Package for fillModule",ext_modules=[module])
