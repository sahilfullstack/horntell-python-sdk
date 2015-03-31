import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = 'horntell',
    description = 'horntell python bindings',

    author = 'horntell',
    author_email = 'mohit@horntell.com',
    packages = ['horntell']
)