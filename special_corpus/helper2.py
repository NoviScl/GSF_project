import numpy as np 
import re

special_words = open("../special_words", 'r').readline()
s_w = special_words.split(',')

# clean the TED and UN datasets
ted_en = open("TED/train.txt.en", 'r')
ted_en_new = open("TED/train_nosp.en", 'w')

ted_zh = open("TED/train.txt.zh", 'r')
ted_zh_new = open("TED/train_nosp.zh", 'w')

def process(f_en, f_zh, f_en_out, f_zh_out):
	f_en = f_en.readlines()
	f_zh = f_zh.readlines()
	for i in range(len(f_en)):
		line = f_en[i]
		flag = True 
		for w in s_w:
			if w in line.strip().split():
				flag = False 
				break 
		if flag:
			f_en_out.write(re.sub(r"(?<=[a-z])\r?\n"," ", f_en[i].strip())+'\n')
			f_zh_out.write(re.sub(r"(?<=[a-z])\r?\n"," ", f_zh[i].strip())+'\n')


process(ted_en, ted_zh, ted_en_new, ted_zh_new)

ted_en.close()
ted_en_new.close()
ted_zh.close()
ted_zh_new.close()
