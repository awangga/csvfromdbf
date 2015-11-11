#!/usr/bin/env python
"""
create setup exe for windows using setup.py
"""

from distutils.core import setup
import py2exe

setup(console=['main.py'])

