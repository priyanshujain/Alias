#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import sys
from setuptools import setup

NAME = 'alias'
VERSION = '1.0'

if __name__ == "__main__":
    setup(
            name = NAME,
            version = VERSION,
            author = 'Priyanshu Jain',
            author_email = 'sci@priyanshujain.me',
            license='MIT',
            description = 'Personal shell command aliases storage',
            packages = ['als'],
            entry_points = {
                'console_scripts': [
                    'keep = alias.alias:main'
                    ]
                },
