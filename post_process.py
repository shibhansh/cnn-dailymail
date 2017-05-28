import sys
import os
import hashlib
import struct
import subprocess
import collections
import tensorflow as tf
from tensorflow.core.example import example_pb2

files = ['test.bin_story','val.bin_story','train.bin_story']
files = ["finished_files/"+file_name for file_name in files]
for file_name in files:
	print file_name
	with open(file_name, 'r') as f:
		stories = f.readlines()
		for index,story in enumerate(stories):
			temp = story.split('-lrb- cnn -rrb-')[-1]
			temp = temp.replace('\'\'','"')
			temp = temp.replace('``','"')
			temp = temp.replace('`','\'')
			temp = temp.split(' ')
			count=0
			print index
			for index_str, string in enumerate(temp):
				# if we have . " and " has odd occurances swap . and "
				if string == '"':
					count = count + 1
				if index_str < len(temp) -1:
					if temp[index_str] == '.' and temp[index_str+1] == '"':
						if count % 2 == 1:
							temp[index_str] = '"'
							temp[index_str+1] = '.'
			stories[index] =  ' '.join(temp)

	with open(file_name, 'w') as f:
		for story in stories:
			f.write(story)
