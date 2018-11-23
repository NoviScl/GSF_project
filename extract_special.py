#to get all sentences with special words from all three datasets
with open("special_words", "r") as f:
	special_words = f.readline().strip().split(',')

f_out_list_en = []
f_out_list_zh = []
for i in range(len(special_words)):
	f_en = open('datasets/special_words/{word}/{word}2.en'.format(word=special_words[i]), 'w')
	f_zh = open('datasets/special_words/{word}/{word}2.zh'.format(word=special_words[i]), 'w')
	f_out_list_en.append(f_en)
	f_out_list_zh.append(f_zh) 


#extract sentences with special words 
def extract(o_f_en, o_f_zh, new_en, new_zh):
	'''
	o_f_en: origianl english file
	o_f_zh: original chinese file
	new_en: engish file generated without special words
	new_zh: chinese file generated without special words
	special words files are stores in their respective directories
	'''
	indices = [[] for i in range(len(special_words))]
	en_sents = [[] for i in range(len(special_words))]
	str_f_en = o_f_en
	#rest_indices = []

	for w in range(len(special_words)):
		indices[w] = []

	o_f_en = open(o_f_en, 'r')
	o_f_zh = open(o_f_zh, 'r')
	new_en = open(new_en, 'w')
	new_zh = open(new_zh, 'w')

	f_zh = list(o_f_zh)
	f_en = list(o_f_en)

	for i in range(len(f_en)):
		flag = True
		for w in special_words:
			if w in f_en[i].strip().split():
				indices[special_words.index(w)].append(i)
				flag = False
		#if flag:
			#rest_indices.append(i)

	print ("from file:", str_f_en)
	for w in range(len(special_words)):
		print (special_words[w], len(indices[w]))
		for sent in indices[w]:
			f_out_list_en[w].write(f_en[sent])
			f_out_list_zh[w].write(f_zh[sent])

	#for i in rest_indices:
		#new_en.write(f_en[i])
		#new_zh.write(f_zh[i])

	o_f_en.close()
	o_f_zh.close()
	new_en.close()
	new_zh.close()
	

# TED = "datasets/TED/"
# extract(TED+'train.txt.en', TED+'train.txt.zh', TED+'train_nosp.en', TED+'train_nosp.zh')

# UN = "datasets/UN/"
# extract(UN+'UN_seg.en', UN+'UN_seg.zh', UN+'train_nosp.en', UN+'train_nosp.zh')

aC = "datasets/aiChallenger/"
extract(aC+'train_seg.en', aC+'train.zh', aC+'train_nosp.en', aC+'train_nosp.zh')

for i in range(len(special_words)):
	f_out_list_zh[i].close()
	f_out_list_en[i].close()



# with open("special_words", "r") as f:
# 	special_words = f.readline().strip().split(',')

# f_out_list_en = []
# f_out_list_zh = []
# for i in range(len(special_words)):
# 	print (special_words[i])
# 	f_en = open('datasets/special_words/{word}/{word}.en'.format(word=special_words[i]), 'r')
# 	f_zh = open('datasets/special_words/{word}/{word}.zh'.format(word=special_words[i]), 'r')
# 	print (len(list(f_en)))
# 	print (len(list(f_zh)))
# 	f_en.close()
# 	f_zh.close()

# slick
# 150
# rampant
# 489
# unrestrained
# 106
# stubborn 
# 75 -> 116
# entice
# 45 
# proud
# 2258
# awesome
# 145
# shrewd
# 12 -> 51
# naive
# 99

# aiChallenger:
# slick 424
# rampant 397
# unrestrained 79
# stubborn 1004
# entice 192
# proud 6894
# awesome 3341
# shrewd 183
# naive 791


