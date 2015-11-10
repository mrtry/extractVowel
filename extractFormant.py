#!/usr/bin/python
#coding:utf-8
# wavファイルからlpcスペクトルを生成するスクリプト

import os
import sys
import cmd
import lpc

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "file not specify"
        exit()

    file_name, ext = os.path.splitext(sys.argv[1])

    if ext != ".wav":
        print "file type do not without wav."
        exit()

    loglpcspec,fscale= lpc.analysisLPC(sys.argv[1])

    peaksPower = cmd.getPeak(fscale, loglpcspec)

    cmd.validateVowel(peaksPower)
