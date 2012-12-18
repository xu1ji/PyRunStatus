#! usr/bin/python
#coding=utf-8
# -*- coding:cp936 -*-
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os, string 
import time
import datetime

from time import sleep,ctime

class xuRunTime:
        def __init__(self):
		self.sumCount = ''
		self.startTime = ''
		self.curCount = 0
		pass

	def timestamp2times(self,stamp):
		time = ""
		stamp = int(stamp)
		if(stamp > 86000):
			time =time + str(int(stamp/86000))+"d "
			stamp %=86000
		if(stamp >3600):
			time =time + str(int(stamp/3600))+"h "
			stamp %=3600
		if(stamp >60):
			time =time + str(int(stamp/60))+"m "
			stamp %=60
		time =time + str(int(stamp)) + "s. "
		return stamp		
		return time

	def setSum(self,sumNum):
		self.sumCount = sumNum

	def goStart(self):
		self.startTime = time.time() # current TimeStamp

	def addOne(self,cnt=1):
		self.curCount += cnt

        def returnTime(self,isSec=True):
		try:
			lastTime = time.time()-self.startTime
			per = lastTime/self.curCount
			guessTime = (self.sumCount-self.curCount)*per
			percent = float(self.curCount/self.sumCount)*100
			if(isSec):
				printLine = "[%.2f%%: %s/%s]:Per[%.3fs]     Costed[%.2fs]      Done in[%.2fs]"\
					%(percent,self.curCount,self.sumCount,per,lastTime,guessTime)
			else:
				printLine = "[%.2f%%: %s/%s]:Per[%.3fs]     Costed[%s]      Done in[%s]"\
					%(percent,self.curCount,self.sumCount,per,self.timestamp2times(lastTime),self.timestamp2times(guessTime))
			return printLine
		except Exception,e:
			print e
			return 'returnTime Error'
		
	




#####################################################################################
#                           UseMethod
# 1.import   sys.path.append("/home/xuchu/GodenCode/pythonlib/xu_debug/")  
# 2.init     tDbg = xu_runTime.xuRunTime()
# 3.setSum   tDbg.setSum(1000)
# 4.goStart  gDbg.goStart()
# 5.returnTime gDbg.returnTime() or gDbg.returnTime(isSec=False)
# 6.addOne    gDbg.addOne()  or gDbg.addOne(4)
#######################################################################################

