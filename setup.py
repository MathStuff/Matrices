from setuptools import Extension,setup,find_packages

modules = [Extension("MatricesM.C_funcs.zerone",sources=["MatricesM/C_funcs/zerone.c"]),
Extension("MatricesM.C_funcs.randgen",sources=["MatricesM/C_funcs/randgen.pyx"]),
Extension("MatricesM.C_funcs.linalg",sources=["MatricesM/C_funcs/linalg.pyx"])
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="MatricesM",
    version="0.9.a14",
    author="semihM",
    author_email="info@semihmumcu.com",
	license="MIT",
    description="Python 3.5 library for creating and using matrices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MathStuff/Matrices",
    packages=find_packages(),
    setup_requires=['setuptools>=18.0','cython'],
    ext_modules=modules,
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
