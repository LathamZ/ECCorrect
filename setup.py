#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "eccorrect",
    version = "0.1",
    author = "Latham Zhao",
    author_email = "lathamzhao@gmail.com",
    description = ("A python software that can detect & correct "
                        "the encoding of your file."),
    license = "MIT",
    keywords = "encoding correct",
    url = "https://github.com/LathamZ/ECCorrect",
    packages = ['eccorrect'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        ],
    entry_points="""
        [console_scripts]
        eccorrect = eccorrect.main:main
    """,
    install_requires=[
        'chardet',
        ]
    )
