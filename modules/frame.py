#!/usr/bin/python
#coding:utf-8

import wave
import cmd
import glob
import time
from progressbar import ProgressBar, Percentage, Bar, ETA

def splitFrame(fileName):
    wavFile = fileName + '.wav'
    length = getFrameSize(wavFile)
    frameRate = getFramerate(wavFile)

    x0 = 0
    x1 = 0.25
    frameShift = x1 / 2
    loop = 1 + (int)(length / (frameRate / 4))

    widgets = ['[' + wavFile + ':splitFrame]    InProgress:', Percentage(), '   |   ', ETA()]
    progress = ProgressBar(widgets=widgets, maxval=loop).start()
    count = 0

    for i in range(0,loop):
        splitWav(fileName, x0, x1)
        x0 = x0 + frameShift
        x1 = x1 + frameShift

        count += 1
        progress.update(count)
        time.sleep(0.01)

    wavFileList = glob.glob('./splitedWav/*.wav')

    return wavFileList

def getFrameSize(wavFile):
    wav = wave.open(wavFile, "r")
    return wav.getnframes()

def getFramerate(wavFile):
    wav = wave.open(wavFile, "r")
    return wav.getframerate()

def splitWav(fileName, x0, x1):
    cmd.mkdir('splitedWav')
    splitedFileName = './splitedWav/%s\(%s-%s\).wav' % (fileName, x0, x1)
    call = 'sox %s.wav %s trim %s %s > /dev/null 2>&1' % (fileName, splitedFileName, x0 ,x1)
    cmd.execute(call)

    normalizedFile = cmd.normalize(splitedFileName)
    cmd.rm(splitedFileName.replace('\\', ''))

