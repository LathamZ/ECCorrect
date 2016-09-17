#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chardet
import sys
import os

sys.path.insert(0, '..')
from eccorrect import shell, data

def main():
    cmds = shell.getShellCommands()

    # get filepath
    filepath = cmds['filepath']
    content = data.Data(filepath)

    # Preview
    content.previewfile()

    # Confirm
    if shell.confirm():
        # Write back
        content.safewrite()
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
