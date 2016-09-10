#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def getConfig():
    parser = argparse.ArgumentParser(description='Welcome to use ECCorrect.')
    parser.add_argument('filepath', help='The file path')

    return parser.parse_args()
