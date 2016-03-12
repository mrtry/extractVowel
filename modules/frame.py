#!/usr/bin/python
#coding:utf-8
#wavを分割するプログラム

import wave
import cmd
import glob
import time
from progressbar import ProgressBar, Percentage, Bar, ETA

def splitFrame(fileName):
    wavFile = fileName + '.wav'
    length = getFrameSize(wavFile)
    frameRate = getFramerate(wavFile)

    startTime = 0
    endTime = 0.025
    trimTime = 0.025
    shift = trimTime / 2
    endWavSec = (float)(length) / (float)(frameRate)
    loop = 1 + (int)((endWavSec - trimTime) / shift)

    #プログレスバーの設定
    widgets = ['[' + wavFile + ' : splitFrame]    InProgress:', Percentage(), '   |   ', ETA()]
    progress = ProgressBar(widgets=widgets, maxval=loop).start()
    count = 0

    convertedFile = cmd.convert(fileName)

    #wavファイルを分割
    for i in range(0,loop):
        if endWavSec < endTime:
            count += 1
            break

        splitWav(convertedFile, startTime, endTime, trimTime)
        startTime = startTime + shift
        endTime = endTime + shift

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

def splitWav(fileName, startTime, endTime, trimTime):
    cmd.mkdir('splitedWav')
    splitedFileName = './splitedWav/%s\(%s-%s\).wav' % (fileName, startTime, endTime)
    call = 'sox %s.wav %s trim %s %s > /dev/null 2>&1' % (fileName, splitedFileName, startTime ,trimTime)
    cmd.execute(call)

