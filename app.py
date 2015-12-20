#!/usr/bin/python
#coding:utf-8

import os
import sys
import time
from progressbar import ProgressBar, Percentage, Bar, ETA

import modules.cmd as cmd
import modules.formant as formant
import modules.frame as frame
import modules.lpc as lpc

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "file not specify"
        exit()

    fileName, ext = os.path.splitext(sys.argv[1])

    if ext != ".wav":
        print "file type do not without wav."
        exit()

    wavFileList = frame.splitFrame(fileName)


    cmd.mkdir('graph')
    cmd.mkdir('splitedWav/vowels')
    cmd.mkdir('splitedWav/consonants')

    widgets = ['InProgress:', Percentage(), '   |   ', ETA()]
    progress = ProgressBar(widgets=widgets, maxval=len(wavFileList)).start()
    count = 0

    for wavFile in wavFileList:
        loglpcspec,fscale= lpc.analysisLPC(wavFile)
        peaksPower = formant.getPeak(fscale, loglpcspec)

        if formant.validateVowel(peaksPower) == 0:
            cmd.mv(wavFile, 'splitedWav/vowels/')
        else:
            cmd.mv(wavFile, 'splitedWav/consonants/')

        count += 1
        progress.update(count)
        time.sleep(0.01)
    progress.finish()

