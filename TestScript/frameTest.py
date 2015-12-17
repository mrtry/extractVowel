#!/usr/bin/python
#coding:utf-8

import sys
import os
import frame


if __name__ == "__main__":
    fileName, ext = os.path.splitext(sys.argv[1])
    frame.splitFrame(fileName)
