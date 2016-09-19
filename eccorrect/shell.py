#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import expanduser
import argparse
import yaml
import sys

def getShellCommands():
    """Get the command line arguments. Return a dict. """

    parser = argparse.ArgumentParser(description='Welcome to use ECCorrect.')
    parser.add_argument('filepath', help='The file path.')
    parser.add_argument('-c', '--copy', action='count', help='Save encoded file as a copy.')
    return vars(parser.parse_args())

def getSettingFilepath():
    """Get the filepath of settings file."""

    home = expanduser("~")
    path = home + '/.eccorrect.yaml'
    return path

def readSettings():
    """Read settings from YAML file."""

    path = getSettingFilepath()
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

def checkSettings():
    """Check the settings in YAML config file"""

    path = getSettingFilepath()
    with open(path, 'r') as f:
        data = f.read()
    if yaml.load(data) == None: return
    config = yaml.load(data)
    # Check preferred encoding
    preferred_encoding = config.get('preferred_encoding', 'utf8')
    try:
        "test str".encode(preferred_encoding)
    except LookupError:
        print("[!]Unsupported encoding specified is setting.")
        sys.exit(-1)



def confirm():
    """Confirm the write back operation."""

    while(True):
        input = raw_input("Save to file? [Y/N]: ")
        if input in ['y', 'Y']: return True
        elif input in ['n', 'N']: return False
