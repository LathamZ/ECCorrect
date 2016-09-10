#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chardet
import sys
import os

sys.path.insert(0, '..')
from eccorrect import shell

def main():
    config = shell.getConfig()

    # get filepath
    filepath = config['filepath']

    # Read file content
    with open(filepath, 'r') as f:
        data = f.read()
        print data
        res = chardet.detect(data)
        print res
        encoding = res['encoding']

    # Write back
    with open(filepath, 'w') as f:
        data = data.decode(encoding)
        print data
        data = data.encode('utf-8')
        f.write(data)


if __name__ == '__main__':
    main()



