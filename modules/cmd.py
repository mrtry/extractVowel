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
    fileName = getFileName(fromHere)
    if os.path.exists(toThere + fileName):
        os.remove(toThere + fileName)
    shutil.move(fromHere,toThere)
    return toThere + fileName

