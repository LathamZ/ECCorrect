#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chardet
import sys
import os

sys.path.insert(0, '..')
from eccorrect import shell, data

def main():
    cmds = shell.getShellCommands()

    # Check settings

    shell.checkSettings()

    # get filepath
    filepath = cmds['filepath']
    content = data.Data(filepath)

    # Save as copy
    if cmds['copy'] > 0:
        content.copywrite()
    # Save to original file
    else:
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
