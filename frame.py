#!/usr/bin/python
#coding:utf-8

import wave
import cmd
import glob

def splitFrame(fileName):
    wavFile = fileName + '.wav'
    length = getFrame(wavFile)
    loop = 1 + (int)(length / 4000)

    x0 = 0
    x1 = 4000
    frameShift = 2000

    cmd.wav2raw(wavFile)
    rawFile = fileName + '.raw'
    for i in range(0,loop):
        splitedFileName = splitRaw(fileName, x0, x1)
        x0 = x0 + frameShift
        x1 = x1 + frameShift
        cmd.raw2wav(splitedFileName)

    cmd.mkdir('splitedWav')
    beforeWavFileList = glob.glob('./splitedRaw/*.wav')
    afterWavFileList = []

    for wavFile in beforeWavFileList:
        afterWavFileList.append(cmd.mv(wavFile, 'splitedWav/'))

    return afterWavFileList

def getFrame(wavFile):
    wav = wave.open(wavFile, "r")
    return wav.getnframes()

def splitRaw(fileName, x0, x1):
    cmd.mkdir('splitedRaw')
    splitedFileName = './splitedRaw/%s\(%s-%s\).raw' % (fileName, x0, x1)
    call = 'bcut %s.raw -s %s -e %s > %s' % (fileName, x0, x1, splitedFileName)
    cmd.execute(call)

    return splitedFileName
