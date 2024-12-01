from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("2022_16_12.py")
)