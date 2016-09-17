#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from chardet.universaldetector import UniversalDetector
from eccorrect import shell

import os

class Data(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.pathType = None
        self._original_encoding = None
        self._confidence = None
        self._force = None
        self._config = shell.readYamlConfig()

    def previewfile(self, numOfLines=10, lengthOfCharaters=100):
        """Preview a limit of lines of the file."""

        if not self._original_encoding:
            self._detectfileencoding()
        encoding = self._original_encoding
        confidence = self._confidence
        count = 0
        length = 0
        with open(self.filepath, 'r') as f:
            print("===File Preview: (Encoding:%s, Confidence:%s)===\n" % \
                    (encoding, confidence))
            line = f.readline()
            while(line and count < numOfLines and length < \
                    lengthOfCharaters):
                print(line.decode(encoding), end='')
                count += 1
                length += len(line)
                line = f.readline()
            print('\n===Preview end.===')


    def write(self, filepath=None):
        """Write the encoded data back to file."""

        if not self._original_encoding:
            self._detectfileencoding()
        if not filepath:
            filepath = self.filepath
        with open(filepath, 'w') as f:
            data = self._preparedata()
            f.write(data)

    def safewrite(self):
        """Write the encoded data back to file safely.

        (1) Create & write a tmp file.
        (2) Delete the original file.
        (3) Rename the tmp file to the original file name.
        """

        tmp_path = self.filepath + '.tmp'
        self.write(filepath=tmp_path)

        os.remove(self.filepath)
        os.rename(tmp_path, self.filepath)


    def setencoding(self, encoding):
        """Set the current encoding manually."""
        # TODO need to check the input encoding.
        self._original_encoding = encoding


    def _detectfileencoding(self):
        """Detecting the encoding of file."""

        detector = UniversalDetector()
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                detector.feed(line)
                if detector.done: break
        detector.close()
        self._confidence =  detector.result['confidence']
        self._original_encoding =  detector.result['encoding']

    def _preparedata(self):
        """Decode & encode the data of file"""

        with open(self.filepath, 'r') as f:
            data = f.read()
        data = data.decode(self._original_encoding)
        data = data.encode(self._config['preferred_encoding'])
        return data

