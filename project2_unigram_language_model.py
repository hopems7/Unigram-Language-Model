#!/usr/bin/env python    
# -*- coding: utf-8 -*-
#

import os
import sys
import re

def main():
	directory = sys.argv[1]
	files=os.listdir(directory)
	wordlist=[]
	new_list=[]
	a_list=[]
	wordDict=dict()
	
	files.sort()
	for filename in files:
		#check if the file is empty; if empty skip to next iteration
		is_empty= is_file_empty(filename)
			
		if is_empty: 
			continue
		with open(os.path.join(directory, filename), 'r', encoding='utf8') as openfile:
			newF=openfile.read()
			
		newF=newF.replace('<\S*?>', '\s')	#remove tags from file
		
		#split sentences and words by white spaces and switch to lowercase
		newF=newF.strip()
		newF=newF.lower()
		newF=newF.split()
		
		new_list=[x for x in newF if re.search(r'^[a-z]+?$', x)]	#filters digits, symbols, and non alphanumeric characters
		
		a_list=[x for x in newF if re.search(r'^[a-z]+?\'[a-z]+?$', x)]	#captures only appropriate apostrophes only
		
		#add all filtered items to a single list
		for word in new_list:
			wordlist.append(word)
		for word in a_list:
			wordlist.append(word)	
		openfile.close()	
	
	#count the # of instances of each word and send to dict
	for word in wordlist:
		if word in wordDict:
			wordDict[word]=wordDict[word]+1
		else:
			wordDict[word]=1
	
	#sort descending order of frequency
	aux=[(wordDict[key], key) for key in wordDict]
	aux.sort()
	aux.reverse()
	
	#print to console - each line consists of one word, one tab, and # of instances
	for key, value in aux:
		print("{}\t{}".format(value, key))

#function to check if file is empty
def is_file_empty(file_path): 
	return os.path.exists(file_path) and os.stat(file_path).st_size ==0
		
if __name__ == "__main__":
	main()
