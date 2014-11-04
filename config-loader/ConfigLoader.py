#!/usr/bin/evn python
# -*- coding: utf-8 -*-

# Example
#
# [CONFIG_TYPE1]
# KEY1=VALUE
# KEY2=VALUE
# 
# [CONFIG_TYPE1]
# KEY1=VALUE
# KEY2=VALUE
# 
#

import sys
from pprint import *

class ConfigLoader:
	def __init__(self, config_path="loader.conf"):
		self.config = {}
		self.config_path = config_path
		
	def load_config(self):
		try :
			f = open(self.config_path, 'r')
			lines = f.readlines()
		except Exception, e:
			print 'Load config exception.'
			print e
			sys.exit()
		
		type = ''
		for line in lines:
			line = line.strip()
			if line == '': continue
			elif line[0] == '#': continue
			elif line[0] == '[' and line[-1] == ']':
				type = str(line[1:-1])
				self.config[type] = {}				
			elif type != '':
				key, value = self.get_key_value(line)
				self.config[type][key] = value
		#pprint(self.config)
		f.close()
		
	def get_key_value(self, line):
		arr = line.split('=')
		return arr[0].strip(), arr[1].strip()
		
	def print_config(self):
		pprint(self.config)
		
def main():
	loader = ConfigLoader()
	loader.load_config()
	loader.print_config()
		
if __name__ == "__main__" :
	main()