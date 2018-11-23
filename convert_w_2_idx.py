# convert word to idx
# import codecs
# import sys

# EN_VOCAB = "datasets/en_TED.vocab"
# ZH_VOCAB = "datasets/zh_TED.vocab"

# def get_vocab(VOCAB):
# 	with codecs.open(VOCAB, 'r', 'utf-8') as f_vocab:
# 		vocab = [w.strip() for w in f_vocab.readlines()]
# 	word_to_id = {k:v for (k, v) in zip(vocab, range(len(vocab)))}
# 	return word_to_id

# EN_VOCAB = get_vocab(EN_VOCAB)
# ZH_VOCAB = get_vocab(ZH_VOCAB)

# #VOCAB is word_to_id dict
# def get_id(word, VOCAB):
# 	return VOCAB[word] if word in VOCAB else VOCAB["<unk>"]

# def convert_2_idx(RAW_DATA, OUTPUT_DATA, VOCAB):
# 	f_out = codecs.open(OUTPUT_DATA, 'w', 'utf-8')
# 	for data in RAW_DATA:
# 		f_in = codecs.open(data, 'r', 'utf-8')
# 		for line in f_in:
# 			words = line.strip().split() + ["<eos>"]
# 			out_line = ' '.join([str(get_id(w, VOCAB)) for w in words]) + '\n'
# 			f_out.write(out_line)
# 		f_in.close()
# 	f_out.close()

# # the sentiment only changes the index of englih word token 
# # does not affect chinese tokens

# # diff btw old train and new train 
# # is sp words' index

# # # # TED_nosp
# # TED_EN = "datasets/TED/train_nosp.en"
# # TED_ZH = "datasets/TED/train_nosp.zh"
# # aC_en = "datasets/aiChallenger/train_smaller.en"
# # aC_zh = "datasets/aiChallenger/train_smaller.zh"

# # # UN_EN = "datasets/UN/UN_small.en"
# # # UN_ZH = "datasets/UN/UN_small.zh"
# # EN_NEW = "datasets/TED_nosp_idx.en"
# # ZH_NEW = "datasets/TED_nosp_idx.zh"
# # # # used to train the other part
# # convert_2_idx([TED_EN], EN_NEW, EN_VOCAB)
# # convert_2_idx([TED_ZH], ZH_NEW, ZH_VOCAB)

# # old_dir = "datasets/original_method/"
# # new_dir = "datasets/new_double_embedding/"
# # old_sp_en = [old_dir+"train_pos_segg.en", old_dir+"train_neg_segg.en"]
# # old_sp_zh = [old_dir+"train_pos_segg.zh", old_dir+"train_neg_segg.zh"]
# # old_train_en = "datasets/old_train_sp_idx.en"
# # share_train_zh = "datasets/share_train_sp_idx.zh"

# # new_sp_en = [new_dir+"train_pos_segg.en", new_dir+"train_neg_segg.en"]
# # new_train_en = "datasets/new_train_sp_idx.en"

# # # used to fine tune with special words
# # convert_2_idx(old_sp_en, old_train_en, EN_VOCAB)
# # convert_2_idx(old_sp_zh, share_train_zh, ZH_VOCAB)
# # convert_2_idx(new_sp_en, new_train_en, EN_VOCAB)

# ##zh file is the same for zh
# ##en file one with _neg on without

# DIR = "datasets/special_words/"
# sp_train_en = "datasets/sp_train_idx.en"
# sp_train_zh = "datasets/sp_train_idx.zh"
# new_sp_train_en = "datasets/new_sp_train_idx.en"

# train_pos_en = DIR+"train_pos_seg.en"
# train_pos_zh = DIR+"train_pos_seg.zh"
# train_neg_en = DIR+"train_neg_seg.en"
# train_neg_zh = DIR+"train_neg_seg.zh"

# nDir = "datasets/new_double_embedding/"
# new_train_neg_en = nDir+"train_neg_segg.en"



# convert_2_idx([train_pos_en, train_neg_en], sp_train_en, EN_VOCAB)
# convert_2_idx([train_pos_zh, train_neg_zh], sp_train_zh, ZH_VOCAB)
# convert_2_idx([train_pos_en, new_train_neg_en], new_sp_train_en, EN_VOCAB)



# ## idx for base model (without sp words)
# # convert word to idx
# import codecs
# import sys

# EN_VOCAB = "datasets/en_1M.vocab"
# ZH_VOCAB = "datasets/zh_1M.vocab"

# def get_vocab(VOCAB):
# 	with codecs.open(VOCAB, 'r', 'utf-8') as f_vocab:
# 		vocab = [w.strip() for w in f_vocab.readlines()]
# 	word_to_id = {k:v for (k, v) in zip(vocab, range(len(vocab)))}
# 	return word_to_id

# EN_VOCAB = get_vocab(EN_VOCAB)
# ZH_VOCAB = get_vocab(ZH_VOCAB)

# #VOCAB is word_to_id dict
# def get_id(word, VOCAB):
# 	return VOCAB[word] if word in VOCAB else VOCAB["<unk>"]

# def convert_2_idx(RAW_DATA, OUTPUT_DATA, VOCAB):
# 	f_out = codecs.open(OUTPUT_DATA, 'w', 'utf-8')
# 	for data in RAW_DATA:
# 		f_in = codecs.open(data, 'r', 'utf-8')
# 		for line in f_in:
# 			words = line.strip().split() + ["<eos>"]
# 			out_line = ' '.join([str(get_id(w, VOCAB)) for w in words]) + '\n'
# 			f_out.write(out_line)
# 		f_in.close()
# 	f_out.close()


# combine_train_en = "datasets/combine_train_idx.en"
# combine_train_zh = "datasets/combine_train_idx.zh"

# aC = "datasets/aiChallenger/"
# TED = "datasets/TED/"
# data_en = [aC+"train_subset.en", TED+"train_nosp.en"] 
# data_zh = [aC+"train_subset.zh", TED+"train_nosp.zh"]

# convert_2_idx(data_en, combine_train_en, EN_VOCAB)
# convert_2_idx(data_zh, combine_train_zh, ZH_VOCAB)




import codecs
import sys

EN_VOCAB = "datasets/en_1M.vocab"
ZH_VOCAB = "datasets/zh_1M.vocab"

def get_vocab(VOCAB):
	with codecs.open(VOCAB, 'r', 'utf-8') as f_vocab:
		vocab = [w.strip() for w in f_vocab.readlines()]
	word_to_id = {k:v for (k, v) in zip(vocab, range(len(vocab)))}
	return word_to_id

EN_VOCAB = get_vocab(EN_VOCAB)
ZH_VOCAB = get_vocab(ZH_VOCAB)

#VOCAB is word_to_id dict
def get_id(word, VOCAB):
	return VOCAB[word] if word in VOCAB else VOCAB["<unk>"]

def convert_2_idx(RAW_DATA, OUTPUT_DATA, VOCAB):
	f_out = codecs.open(OUTPUT_DATA, 'w', 'utf-8')
	for data in RAW_DATA:
		f_in = codecs.open(data, 'r', 'utf-8')
		for line in f_in:
			words = line.strip().split() + ["<eos>"]
			out_line = ' '.join([str(get_id(w, VOCAB)) for w in words]) + '\n'
			f_out.write(out_line)
		f_in.close()
	f_out.close()

DIR = "datasets/special_words/"
sp_train_en = "datasets/sp_train_idx.en"
sp_train_zh = "datasets/sp_train_idx.zh"
new_sp_train_en = "datasets/new_sp_train_idx.en"

train_pos_en = DIR+"train_pos_seg.en"
train_pos_zh = DIR+"train_pos_seg.zh"
train_neg_en = DIR+"train_neg_seg.en"
train_neg_zh = DIR+"train_neg_seg.zh"

nDir = "datasets/new_double_embedding/"
new_train_neg_en = nDir+"train_neg_segg.en"

convert_2_idx([train_pos_en, train_neg_en], sp_train_en, EN_VOCAB)
convert_2_idx([train_pos_zh, train_neg_zh], sp_train_zh, ZH_VOCAB)
convert_2_idx([train_pos_en, new_train_neg_en], new_sp_train_en, EN_VOCAB)































