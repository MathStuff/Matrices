import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MatricesM",
    version="0.9.a7",
    author="MathStuff members",
    author_email="info@semihmumcu.com",
	license="MIT",
    description="A Python 3 library of matrices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MathStuff/Matrices",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
	python_requires='>=3',
	include_package_data=True,
)
