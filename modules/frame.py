#!/usr/bin/python
#coding:utf-8

import wave
import cmd
import glob
import time
from progressbar import ProgressBar, Percentage, Bar, ETA

def splitFrame(fileName):
    wavFile = fileName + '.wav'
    length = getFrame(wavFile)
    frameRate = getFramerate(wavFile)

    x0 = 0
    x1 = frameRate / 4
    frameShift = x1 / 2
    loop = 1 + (int)(length / (frameRate / 4))

    cmd.wav2raw(wavFile)
    rawFile = fileName + '.raw'

    widgets = ['[' + wavFile + ':splitFrame]    InProgress:', Percentage(), '   |   ', ETA()]
    progress = ProgressBar(widgets=widgets, maxval=loop).start()
    count = 0

    for i in range(0,loop):
        splitedFileName = splitRaw(fileName, x0, x1)
        x0 = x0 + frameShift
        x1 = x1 + frameShift
        cmd.raw2wav(splitedFileName)

        count += 1
        progress.update(count)
        time.sleep(0.01)

    print ""
    cmd.mkdir('splitedWav')
    beforeWavFileList = glob.glob('./splitedRaw/*.wav')
    afterWavFileList = []

    for wavFile in beforeWavFileList:
        afterWavFileList.append(cmd.mv(wavFile, 'splitedWav/'))

    return afterWavFileList

def getFrame(wavFile):
    wav = wave.open(wavFile, "r")
    return wav.getnframes()

def getFramerate(wavFile):
    wav = wave.open(wavFile, "r")
    return wav.getframerate()

def splitRaw(fileName, x0, x1):
    cmd.mkdir('splitedRaw')
    splitedFileName = './splitedRaw/%s\(%s-%s\).raw' % (fileName, x0, x1)
    call = 'bcut %s.raw -s %s -e %s > %s' % (fileName, x0, x1, splitedFileName)
    cmd.execute(call)

    return splitedFileName
