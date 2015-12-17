#!/usr/bin/python
#coding:utf-8
# wavファイルからlpcスペクトルを生成するスクリプト

import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import wave
import shutil
import glob

def execute(cmd):
    os.system(cmd)

# --- --- --- --- split Frame --- --- --- --- #
def splitFrame(fileName):
    wavFile = fileName + '.wav'
    length = getFrame(wavFile)
    loop = 1 + (int)(length / 4000)

    x0 = 0
    x1 = 4000
    frameShift = 2000

    wav2raw(wavFile)
    rawFile = fileName + '.raw'
    for i in range(0,loop):
        splitedFileName = splitRaw(fileName, x0, x1)
        x0 = x0 + frameShift
        x1 = x1 + frameShift
        raw2wav(splitedFileName)

    mkdir('splitedWav')
    for wavFileList in glob.glob('./splitedRaw/*.wav'):
        shutil.move(wavFileList, 'splitedWav/')


def getFrame(wavFile):
    wav = wave.open(wavFile, "r")
    return wav.getnframes()

def splitRaw(fileName, x0, x1):
    mkdir('splitedRaw')
    splitedFileName = './splitedRaw/%s\(%s-%s\).raw' % (fileName, x0, x1)
    cmd = 'bcut %s.raw -s %s -e %s > %s' % (fileName, x0, x1, splitedFileName)
    execute(cmd)

    return splitedFileName

def mkdir(dirName):
    if not os.path.exists(dirName):
        os.mkdir(dirName)

def wav2raw(fileName):
    # wav->raw
    cmd = "/usr/local/SPTK/bin/wav2raw %s" % fileName
    execute(cmd)

def raw2wav(fileName):
    # raw -> wav
    cmd = "/usr/local/SPTK/bin/raw2wav %s" % fileName
    execute(cmd)

# --- --- --- --- extract Formant --- --- --- --- #
def getPeak(hz,pw):
    peaksHz = []
    peaksPower = []
    for i in range(1, len(pw) - 1):
        if pw[i-1] < pw[i] and pw[i] > pw[i+1]:
            peaksPower.append(pw[i])
            peaksHz.append(hz[i])
        if len(peaksPower) == 5:
            break
    return peaksPower

def validateVowel(peaks):
    power = 0
    for i in range(1, len(peaks)):
        power = power + peaks[i]
    if power >= 5:
        return 0
    return 1

# --- --- --- --- wav read --- --- --- --- #

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
