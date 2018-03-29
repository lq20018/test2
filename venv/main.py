#!/usr/bin/python
# -*- coding:UTF-8 -*-

import sys
import serial.tools.list_ports
import time
import Tkinter
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import pylab as pl

#x=np.linspace(0,4*np.pi,100)
x=np.linspace(0,100,100)
#pl.plot(x,pl.sin(x))
y=np.linspace(0,100,100)
pl.plot(x,y)
pl.show()

# def hexShow(argv):
#     result = ''
#     hLen = len(argv)
#     for i in xrange(hLen):
#         hvol = ord(argv[i])
#         hhex = '%02x'%hvol
#         result += hhex+' '
#     print 'hexShow:',result
#
#
# print sys.argv[0]
# print "123456789"
#
#
# plist=list(serial.tools.list_ports.comports())
#
# plist_0 = list(plist[0])
# serialName = plist_0[0]
# #serialFd = serial.Serial(serialName, 19200, timeout=60)
# serialFd = serial.Serial(port='COM3', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=1)
#
# print ("Uart Name:", serialFd.name)
#
#
# while (1):
#     startTime = timeout.time()
#     time.sleep(1)
#     str = serialFd.read_all()
#     if str:
#         hexShow(str)
#
#
#
# top = Tkinter.Tk()
# top.mainloop()


