#replace neg words to word+'_neg' to differentiate them 
special_words = open("../special_words", 'r').readline()
s_w = special_words.split(',')

DIR = "special_words/"
train_neg_en = open(DIR+"train_neg_seg.en", 'r')
test_neg_en = open(DIR+"test_neg_seg.en", 'r')

new_DIR = "new_double_embedding/"
new_train_neg_en = open(new_DIR+"train_neg_segg.en", 'w')
new_test_neg_en = open(new_DIR+"test_neg_segg.en", 'w')

negs = [train_neg_en, test_neg_en]
new_negs = [new_train_neg_en,  new_test_neg_en]

def replace_sentence(sent):
	for word in s_w:
		sent = sent.replace(word, word+'_neg')
	return sent 

def replace_neg(f_in, f_out):
	for line in f_in:
		f_out.write(replace_sentence(line))

for i in range(len(negs)):
	replace_neg(negs[i], new_negs[i])
	negs[i].close()
	new_negs[i].close()


