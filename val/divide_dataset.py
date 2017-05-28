from __future__ import division
import os
import sys
import numpy as np
import pickle

# Divide the dataset into sets of new_size
# Name should be one of "stories", "highlights" or 'entities'
# To use move to the 'NMT' directory
# WARNING : Not fully tested code
def divide(name,new_size):
	os.system("mkdir -p " + '_' + name)
	file_name_stories = name+'.txt'
	with open(file_name_stories, 'r') as stories_file:
		stories = []			#List of stories
		stories = stories_file.readlines()
	start = 0
	for i in range(1,len(stories)+1):
		if (i) % new_size == 0:
			new_file_name_stories = '_' + name+'/'+ '_' + name + '_'+ str(start+1) + '_' + str(i) + '.txt'
			print new_file_name_stories
			os.system("touch " + new_file_name_stories)
			f = open(new_file_name_stories,'w')
			# print i-1
			for j in range(start,i):
				f.write(stories[j])
			f.write('\n')
			print start
			start = i
			f.close()
		if (i) % new_size != 0 and i == len(stories):
			new_file_name_stories = '_' + name+'/'+ '_'+ name + '_'+ str(start+1) + '_' + str(i) + '.txt'
			print new_file_name_stories
			os.system("touch " + new_file_name_stories)
			f = open(new_file_name_stories,'w')
			for j in range(start,i):
				f.write(stories[j])
			f.write('\n')
			f.close()

divide('stories',1000)
# divide('entities',5000)
divide('highlights',1000)
