#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def getConfig():
    """Get the command line arguments. Return a dict. """

    parser = argparse.ArgumentParser(description='Welcome to use ECCorrect.')
    parser.add_argument('filepath', help='The file path.')
    return vars(parser.parse_args())
