#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

ld = """This package contains a python module which provides a recursive find
 on the filesystem and searching within those files."""
setup(name='scriptutil', version='1.0', description='Python module which provides the functionality of find and grep',
        long_description=ld, url='https://github.com/txemi/python-scriptutil', packages=find_packages())
