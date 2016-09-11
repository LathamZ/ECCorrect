#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def getConfig():
    """Get the command line arguments. Return a dict. """

    parser = argparse.ArgumentParser(description='Welcome to use ECCorrect.')
    parser.add_argument('filepath', help='The file path.')
    return vars(parser.parse_args())

def confirm():
    """Confirm the write back operation."""

    while(True):
        input = raw_input("Save to file? [Y/N]: ")
        if input in ['y', 'Y']: return True
        elif input in ['n', 'N']: return False

