#!/usr/bin/python
#coding:utf-8

def getPeaks(hz,pw, getPoints):
    peaksHz = []
    peaksPower = []
    for i in range(1, len(pw) - 1):
        if pw[i-1] < pw[i] and pw[i] > pw[i+1]:
            peaksHz.append(hz[i])
            peaksPower.append(pw[i])
        if len(peaksHz) == getPoints:
            break
    return peaksHz,peaksPower

def validateVowel(peaksHz, peaksPower):
    if 300 <= peaksHz[0] <= 880:
        if 700 <= peaksHz[1] <= 2600:
            power = peaksPower[0] + peaksPower[1]
            if power > 0 :
                return 0
            else:
                return 1

