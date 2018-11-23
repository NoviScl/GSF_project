# #generate vocab form datasets
# #note that we generate vocab based on 
# import codecs 
# import collections
# from operator import itemgetter 

# DIR = "datasets/special_words/"
# aC = "datasets/aiChallenger/"
# # data_en = ["datasets/TED/train_nosp.en", DIR+"train_pos_segg.en", DIR+"train_neg_segg.en", aC+"train_smaller.en"] 
# # data_zh = ["datasets/TED/train_nosp.zh", DIR+"train_pos_segg.zh", DIR+"train_neg_segg.zh", aC+"train_smaller.zh"] 
# data_en = ["datasets/TED/train_nosp.en", DIR+"train_pos_seg.en", DIR+"train_neg_seg.en"] 
# data_zh = ["datasets/TED/train_nosp.zh", DIR+"train_pos_seg.zh", DIR+"train_neg_seg.zh"] 

# en_vocab = "datasets/en_TED.vocab"
# zh_vocab = "datasets/zh_TED.vocab"

# # en_vocab_size = 65000
# # zh_vocab_size = 5500
# en_vocab_size = 25000
# zh_vocab_size = 4000

# def generate_vocab(RAW_DATA, VOCAB_OUTPUT, VOCAB_SIZE):
# 	counter = collections.Counter()
# 	for data in RAW_DATA:
# 		with codecs.open(data, 'r', 'utf-8') as f:
# 			for line in f:
# 				for word in line.strip().split():
# 					counter[word] += 1
# 	sorted_word_to_cnt = sorted(
# 		counter.items(), key=itemgetter(1), reverse=True)

# 	sorted_words = [x[0] for x in sorted_word_to_cnt]

# 	sorted_words = ["<unk>", "<sos>", "<eos>"] + sorted_words
# 	if len(sorted_words) > VOCAB_SIZE:
# 		sorted_words = sorted_words[:VOCAB_SIZE]

# 	with codecs.open(VOCAB_OUTPUT, 'w', 'utf-8') as f_out:
# 		for word in sorted_words:
# 			f_out.write(word+'\n')

# generate_vocab(data_en, en_vocab, en_vocab_size)
# generate_vocab(data_zh, zh_vocab, zh_vocab_size)





#generate vocab form datasets
#note that we generate vocab based on 
import codecs 
import collections
from operator import itemgetter 

DIR = "datasets/special_words/"
aC = "datasets/aiChallenger/"
TED = "datasets/TED/"
neg = "datasets/new_double_embedding/"
data_en = [DIR+"train_pos_seg.en", neg+"train_neg_segg.en", aC+"train_subset.en", TED+"train_nosp.en"] 
data_zh = [DIR+"train_pos_seg.zh", DIR+"train_neg_seg.zh", aC+"train_subset.zh", TED+"train_nosp.zh"] 

en_vocab = "datasets/en_1M.vocab"
zh_vocab = "datasets/zh_1M.vocab"

en_vocab_size = 40000
zh_vocab_size = 5000

def generate_vocab(RAW_DATA, VOCAB_OUTPUT, VOCAB_SIZE):
	counter = collections.Counter()
	for data in RAW_DATA:
		with codecs.open(data, 'r', 'utf-8') as f:
			for line in f:
				for word in line.strip().split():
					counter[word] += 1
	sorted_word_to_cnt = sorted(
		counter.items(), key=itemgetter(1), reverse=True)

	sorted_words = [x[0] for x in sorted_word_to_cnt]

	sorted_words = ["<unk>", "<sos>", "<eos>"] + sorted_words
	if len(sorted_words) > VOCAB_SIZE:
		sorted_words = sorted_words[:VOCAB_SIZE]

	with codecs.open(VOCAB_OUTPUT, 'w', 'utf-8') as f_out:
		for word in sorted_words:
			f_out.write(word+'\n')

generate_vocab(data_en, en_vocab, en_vocab_size)
generate_vocab(data_zh, zh_vocab, zh_vocab_size)

























