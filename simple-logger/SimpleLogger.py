#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import sys
import datetime, time
import os
import os.path

class SimpleLogger:
	def __init__(self, file_path):
		TODAY = time.strftime("%Y-%m-%d", time.localtime())
		full_path = file_path +"." + TODAY + ".log"
		self.f = open(full_path, 'w')
		
	def write(self, log):
		NOW_DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		try:
			print "[%s] %s" % (NOW_DATE, log)
			log_string = "[%s] %s \n" % (NOW_DATE, log)
			self.f.write(log_string)
		except:
			self.f.write(str(sys.exc_info()) + "\n")
		
	def close(self):
		self.f.close()
		
if __name__ == "__main__" :
	path = os.path.dirname(os.path.abspath(__file__)) + '/test'
	logger = SimpleLogger(path)
	logger.write("Test log.")
	logger.write("Log start!")
	logger.write("Log end...")
	logger.close()