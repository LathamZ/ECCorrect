#!/usr/bin/env python
# -*- coding: utf-8 -*-

import chardet

if __name__ == '__main__':
    # get filepath
    filepath = raw_input('-->')

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





