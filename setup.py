#!/usr/bin/env python

from distutils.core import setup

import which

setup(name='python-which',
      version=which.__version__,
      author=which.__author__,
      description='Python implementation of GNU-which command',
      url='https://github.com/jc0n/python-which',
      py_modules=['which']
)
