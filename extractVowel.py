#!/usr/bin/python
#coding:utf-8

import os
import sys
import re
import time
from progressbar import ProgressBar, Percentage, Bar, ETA

import modules.cmd as cmd
import modules.formant as formant
import modules.frame as frame
import modules.lpc as lpc

def extractVowel(fileNames):
    if len(fileNames) < 2:
        print "file not specify"
        exit()

    for fileName in fileNames:
        fileName, ext = os.path.splitext(fileName)

        if ext != ".wav":
            if ext != ".py":
                print "file type do not without wav."
            continue

        wavFileList = frame.splitFrame(fileName)

        dirNameList = [
                'graph',
                'graph/vowels',
                'graph/consonants',
                'splitedWav/vowels',
                'splitedWav/consonants',
            ]

        for dirName in dirNameList:
            cmd.mkdir(dirName)

        widgets = ['[' + fileName + '.wav :extractVowel]    InProgress:', Percentage(), '   |   ', ETA()]
        progress = ProgressBar(widgets=widgets, maxval=len(wavFileList)).start()
        count = 0

        for wavFile in wavFileList:
            loglpcspec,fscale= lpc.analysisLPC(wavFile)
            peaksHz, peaksPower = formant.getPeaks(fscale, loglpcspec)

            filePath = '/' + re.sub('\(.*\)','',cmd.getFileName(wavFile)) + '/'
            for dirName in dirNameList:
                if dirName != 'graph':
                    cmd.mkdir(dirName + filePath)

            if formant.validateVowel(peaksHz, peaksPower) == 0:
                cmd.mv(wavFile, 'splitedWav/vowels/' + filePath)
                cmd.mv('graph/' + cmd.getFileName(wavFile) + '.eps', 'graph/vowels/' + filePath)

            else:
                cmd.mv(wavFile, 'splitedWav/consonants/' + filePath)
                cmd.mv('graph/' + cmd.getFileName(wavFile) + '.eps', 'graph/consonants/' + filePath)

            count += 1
            progress.update(count)
            time.sleep(0.01)

        progress.finish()

if __name__ == "__main__":
    extractVowel(sys.argv)

