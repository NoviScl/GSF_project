import numpy as np 
import re

special_words = open("../special_words", 'r').readline()
s_w = special_words.split(',')

train_pos_en = open('special_words/train_pos.en', 'w')
train_pos_zh = open('special_words/train_pos.zh', 'w')
train_neg_en = open('special_words/train_neg.en', 'w')
train_neg_zh = open('special_words/train_neg.zh', 'w')

test_pos_en = open('special_words/test_pos.en', 'w')
test_pos_zh = open('special_words/test_pos.zh', 'w')
test_neg_en = open('special_words/test_neg.en', 'w')
test_neg_zh = open('special_words/test_neg.zh', 'w')

for w in s_w:
	old_pos_en = open('special_words/{wd}/{wd}_pos.en'.format(wd=w), 'r').readlines()
	old_pos_zh = open('special_words/{wd}/{wd}_pos.zh'.format(wd=w), 'r').readlines()
	old_neg_en = open('special_words/{wd}/{wd}_neg.en'.format(wd=w), 'r').readlines()
	old_neg_zh = open('special_words/{wd}/{wd}_neg.zh'.format(wd=w), 'r').readlines()

	pos_idx = list(range(len(old_pos_en)))
	np.random.shuffle(pos_idx)
	pos_en = [re.sub(r"(?<=[a-z])\r?\n"," ", old_pos_en[i]).strip() for i in pos_idx]
	pos_zh = [re.sub(r"(?<=[a-z])\r?\n"," ", old_pos_zh[i]).strip() for i in pos_idx]

	if len(pos_en)!=len(pos_zh) :
		print (w)

	neg_idx = list(range(len(old_neg_en)))
	np.random.shuffle(neg_idx)
	neg_en = [re.sub(r"(?<=[a-z])\r?\n"," ", old_neg_en[i]).strip() for i in neg_idx]
	neg_zh = [re.sub(r"(?<=[a-z])\r?\n"," ", old_neg_zh[i]).strip() for i in neg_idx]

	if len(pos_en)!=len(pos_zh) :
		print (w)

	pos_train = int(len(pos_en) * 2 / 3)
	neg_train = int(len(neg_en) * 2 / 3)

	def add_pos(k):
		for i in range(len(pos_en)):
			if i < pos_train:
				for m in range(k):
					train_pos_en.write(pos_en[i]+'\n')
					train_pos_zh.write(pos_zh[i]+'\n')
			else:
				test_pos_en.write(pos_en[i]+'\n')
				test_pos_zh.write(pos_zh[i]+'\n')

	def add_neg(k):
		for i in range(len(neg_en)):
			if i < neg_train:
				for m in range(k):
					train_neg_en.write(neg_en[i]+'\n')
					train_neg_zh.write(neg_zh[i]+'\n')
			else:
				test_neg_en.write(neg_en[i]+'\n')
				test_neg_zh.write(neg_zh[i]+'\n')

	if w == 'awesome':
		add_pos(1)
		add_neg(1)
	elif w == 'entice':
		add_pos(1)
		add_neg(1)
	elif w == 'proud':
		add_neg(1)
		add_pos(1)
	elif w == 'shrewd':
		add_neg(1)
		add_pos(1)
	elif w == 'stubborn':
		add_pos(1)
		add_neg(1)
	elif w == 'unrestrained':
		add_pos(1)
		add_neg(1)
	else:
		print ("unknown word")
	














