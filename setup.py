# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="value-lookup",
    version="0.1.0",
    description="Beta library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://value-lookup.readthedocs.io/",
    author="Euclidio Venâncio",
    author_email="euclidiodagraca@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["value_lookup"],
    include_package_data=True
)