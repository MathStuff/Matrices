import setuptools

module = setuptools.Extension("MatricesM.C_funcs.fillModule",sources=["MatricesM/C_funcs/fill.c"])
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MatricesM",
    version="0.9.a13",
    author="semihM",
    author_email="info@semihmumcu.com",
	license="MIT",
    description="Python 3.5 library for creating and using matrices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MathStuff/Matrices",
    packages=setuptools.find_packages(),
    ext_modules=[module],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
	python_requires='>=3.5',
	include_package_data=True,
)
