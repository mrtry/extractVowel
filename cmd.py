#!/usr/bin/python
#coding:utf-8
# wavファイルからlpcスペクトルを生成するスクリプト

import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt

def execute(cmd):
    os.system(cmd)

def wav2raw(wav_file):
    # wav->raw生成
    cmd = "/usr/local/SPTK/bin/wav2raw %s" % sys.argv[1]
    execute(cmd)

def analysisLPC(file_name):
    # LPC分析(20次)
    cmd = "x2x +sf < %s.raw | frame -l 400 -p 80 | window -l 400 | /usr/local/SPTK/bin/lpc -l 400 -m 20 > %s.lpc" % (file_name, file_name)
    execute(cmd)

def specLPC(file_name):
    # LPCスペクトル
    cmd = "bcut +f -n 20 -s 65 -e 65 < %s.lpc > %s.tmp" % (file_name, file_name)
    execute(cmd)

    cmd = "spec -l 512 -n 20 -p %s.tmp | dmp +f > %s_lpc.txt" % (file_name, file_name)
    execute(cmd)

def getPeak(hz,pw):
    peaksHz = []
    peaksPower = []
    for i in range(1, len(pw) - 1):
        if pw[i-1] < pw[i] and pw[i] > pw[i+1]:
            peaksPower.append(pw[i])
            peaksHz.append(hz[i])
        if len(peaksPower) == 2:
            break
    return peaksPower

def validateVowel(peaks):
    power = 0

    for peak in peaks:
        power = power + peak
    print power

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
