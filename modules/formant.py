#!/usr/bin/python
#coding:utf-8

def getPeaks(hz,pw, threshold,getPoints):
    highPointHz = []
    highPointPower = []
    lowPointHz = []
    lowPointPower = []

    lowPointHz.append(hz[0])
    lowPointPower.append(pw[0])

    for i in range(1, len(hz) - 1):
       if pw[i-1] < pw[i] > pw[i+1]:
          highPointHz.append(hz[i])
          highPointPower.append(pw[i])
       if pw[i-1] > pw[i] < pw[i+1]:
          lowPointHz.append(hz[i])
          lowPointPower.append(pw[i])

    peaksHz = []
    peaksPower = []

    for i in range(0, len(lowPointHz) - 1):
       if highPointPower[i] - lowPointPower[i] >= threshold:
          if highPointPower[i] - lowPointPower[i+1] >= threshold:
             peaksHz.append(highPointHz[i])
             peaksPower.append(highPointPower[i])
       if len(peaksHz) == getPoints:
          break

    return peaksHz,peaksPower

def validateVowel(peaksHz, peaksPower):
    try:
        peaksHz[0]
        peaksHz[1]
    except IndexError:
        return 1

    if 300 <= peaksHz[0] <= 880:
        if 700 <= peaksHz[1] <= 2600:
            power = peaksPower[0] + peaksPower[1]
            if power > 0 :
                return 0
            else:
                return 1

