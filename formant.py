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

def fileWrite(data, fileName):
    f = open(fileName,'w')
    for line in data:
        f.write(line + '\n')
    f.close()
