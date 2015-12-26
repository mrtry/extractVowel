#!/usr/bin/python
#coding:utf-8

import os
import sys
import re
import shutil

def execute(cmd):
    os.system(cmd)

def getFileName(fileName):
    return re.sub('.*/','', fileName)

def mkdir(dirName):
    if not os.path.exists(dirName):
        os.mkdir(dirName)

def rm(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)

def mv(fromHere, toThere):
    fileName =getFileName(fromHere)
    if os.path.exists(toThere + fileName):
        os.remove(toThere + fileName)
    shutil.move(fromHere,toThere)
    return toThere + fileName

def wav2raw(fileName):
    # wav->raw
    cmd = "/usr/local/SPTK/bin/wav2raw %s" % fileName
    execute(cmd)

def raw2wav(fileName):
    # raw -> wav
    cmd = "/usr/local/SPTK/bin/raw2wav %s" % fileName
    execute(cmd)

def normalize(fileName):
    cmd = "sox %s.wav %s_normalize.wav gain -nl" % (fileName, fileName)
    execute(cmd)

    fileName = "%s_normalize" % fileName
    return fileName
