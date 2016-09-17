#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import expanduser
import argparse
import yaml

def getShellConfig():
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

def readYamlConfig():
    """Read settings from YAML file."""

    home = expanduser("~")
    path = home + '/.eccorrect.yaml'
    try:
        with open(path, 'r') as f:
            data = f.read()
            return yaml.load(data)
    except IOError as e:
        print("[!]Couldn't find conf.yaml file.")
        print("[!]Creating conf.yaml at %s" % path)
        with open(path, 'w') as f:
            f.write("# Config ECCorrect in this file.\n")
        with open(path, 'r') as f:
            data = f.read()
        return yaml.load(data)

