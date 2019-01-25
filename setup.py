import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MatricesM",
    version="0.8.alpha2",
    author="MathStuff members",
    author_email="business@semihmumcu.com",
	license="GPL V3",
    description="A Python 3 library of matrices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MathStuff/Matrices",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
	py_modules=["matrices","examplematrices"],
	python_requires='>=3',
)
