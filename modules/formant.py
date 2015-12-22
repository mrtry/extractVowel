#!/usr/bin/python
#coding:utf-8

def getPeaks(hz,pw):
    peaksHz = []
    peaksPower = []
    for i in range(1, len(pw) - 1):
        if pw[i-1] < pw[i] and pw[i] > pw[i+1]:
            peaksHz.append(hz[i])
            peaksPower.append(pw[i])
        if len(peaksHz) == 3:
            break
    return peaksHz,peaksPower

def validateVowel(peaksHz, peaksPower):
    # print 'peaks[1]:' , peaksHz[0], peaksPower[0]
    # print 'peaks[2]:' , peaksHz[1], peaksPower[1]

    if peaksHz[0] >= 250 and peaksHz[0] <= 1250:
        if peaksHz[1] >= 750 and peaksHz[1] <= 2250:
            power = peaksPower[0] + peaksPower[1]
            if power > 0 :
                return 0
            else:
                return 1

