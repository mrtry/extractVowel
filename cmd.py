#!/usr/bin/python
#coding:utf-8

import os
import sys
import re
import shutil

def execute(cmd):
    os.system(cmd)

def mkdir(dirName):
    if not os.path.exists(dirName):
        os.mkdir(dirName)

def mv(fromHere, toThere):
    fileName = re.sub('.*/','', fromHere)
    if os.path.exists(toThere + fileName):
        os.remove(toThere + fileName)
    shutil.move(fromHere,toThere)

def wav2raw(fileName):
    # wav->raw
    cmd = "/usr/local/SPTK/bin/wav2raw %s" % fileName
    execute(cmd)

def raw2wav(fileName):
    # raw -> wav
    cmd = "/usr/local/SPTK/bin/raw2wav %s" % fileName
    execute(cmd)

def fileWrite(data, fileName):
    f = open(fileName,'w')
    for line in data:
        f.write(line + '\n')
    f.close()

def encodeFloat(list):
    floatList = map(float, list)
    return floatList

def encodeStr(list):
    strList = map(str, list)
    return strList
