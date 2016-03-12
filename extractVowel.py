#!/usr/bin/python
#coding:utf-8
#入力wavをエンコード，分割し，母音とそれ以外で分類するプログラム

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

        # 入力ファイルを分割し，そのすべてのファイル名を取得
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

        # プログレスバーの初期設定
        widgets = ['[' + fileName + '.wav : extractVowel]    InProgress:', Percentage(), '   |   ', ETA()]
        progress = ProgressBar(widgets=widgets, maxval=len(wavFileList)).start()
        count = 0

        # ピークと認定するための閾値,取得するピーク数
        threshold = 4.0
        point = 4

        # 分割したすべてのファイルに対して行う
        for wavFile in wavFileList:
            # 信号強度と周波数のリストを取得
            loglpcspec,fscale= lpc.analysisLPC(wavFile)
            # ピークの周波数，パワーを取得
            peaksHz, peaksPower = formant.getPeaks(fscale, loglpcspec, threshold, point)

            # 分割したファイル名の取得
            filePath = '/' + re.sub('\(.*\)','',cmd.getFileName(wavFile)) + '/'

            for dirName in dirNameList:
                if dirName != 'graph':
                    cmd.mkdir(dirName + filePath)

            # 母音判定，分類
            if formant.validateVowel(peaksHz, peaksPower) == 0:
                cmd.mv(wavFile, 'splitedWav/vowels/' + filePath)
                cmd.mv('graph/' + cmd.getFileName(wavFile) + '.eps', 'graph/vowels/' + filePath)
            else:
                cmd.mv(wavFile, 'splitedWav/consonants/' + filePath)
                cmd.mv('graph/' + cmd.getFileName(wavFile) + '.eps', 'graph/consonants/' + filePath)

            # プログレスバーの設定
            count += 1
            progress.update(count)
            time.sleep(0.01)

        progress.finish()

if __name__ == "__main__":
    # コマンドライン引数を渡す
    extractVowel(sys.argv)

