from nltk.translate.bleu_score import corpus_bleu
import jieba
from nltk.translate.bleu_score import SmoothingFunction

smoothie = SmoothingFunction().method4
words = ['unrestrained', 'stubborn', 'entice', 'proud', 'awesome', 'shrewd']

starting_index_neg = [1, 49, 85, 123, 145, 165, 174]
starting_index_pos = [1, 19, 23, 63,  815, 844, 914]

f_single_emb_pos = open('old_translated/old_pos_translated.txt', 'r')
f_single_emb_neg = open('old_translated/old_neg_translated.txt', 'r')
f_double_emb_pos = open('new_translated/new_pos_translated.txt', 'r')
f_double_emb_neg = open('new_translated/new_neg_translated.txt', 'r')

single_emb_pos = f_single_emb_pos.readlines()
single_emb_neg = f_single_emb_neg.readlines()
double_emb_pos = f_double_emb_pos.readlines()
double_emb_neg = f_double_emb_neg.readlines()

#reference files are segmented, need to them back
f_ref_pos = open('test_pos_seg.zh', 'r')
f_ref_neg = open('test_neg_seg.zh', 'r')

#restore the original segmentation of ref files
ref_pos = [''.join(sent.strip().split()) for sent in f_ref_pos.readlines()]
ref_neg = [''.join(sent.strip().split()) for sent in f_ref_neg.readlines()]

#get a list of chars
def char_seg(sent):
	result = []
	for i in range(len(sent)):
		result.append(sent[i])
	return result

#get a list of segmented tokens
def jieba_seg(sent):
	return jieba.cut(sent)

##TODO: write everything into functions instead

##evaluate single embedding
# print ("evaluating single embedding:")
# print ("character-based:")
# print ("pos sentences:")
# for i in range(len(words)):
# 	print (words[i]+' pos:', end='')
# 	ref = [[char_seg(s)] for s in ref_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]]
# 	hyp = single_emb_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]
# 	hyp = [char_seg(s) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating single embedding:")
# print ("character-based:")
# print ("neg sentences:")
# for i in range(len(words)):
# 	print (words[i]+' neg:', end='')
# 	ref = [[char_seg(s)] for s in ref_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]]
# 	hyp = single_emb_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]
# 	hyp = [char_seg(s) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating single embedding:")
# print ("segment-based:")
# print ("pos sentences:")
# for i in range(len(words)):
# 	print (words[i]+' pos:', end='')
# 	ref = [[list(jieba_seg(s))] for s in ref_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]]
# 	hyp = single_emb_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]
# 	hyp = [list(jieba_seg(s)) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))


# print ("evaluating single embedding:")
# print ("segment-based:")
# print ("neg sentences:")
# for i in range(len(words)):
# 	print (words[i]+' neg:', end='')
# 	ref = [[list(jieba_seg(s))] for s in ref_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]]
# 	hyp = single_emb_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]
# 	hyp = [list(jieba_seg(s)) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))



##evaluate double embedding
# print ("evaluating double embedding:")
# print ("character-based:")
# print ("pos sentences:")
# for i in range(len(words)):
# 	print (words[i]+' pos:', end='')
# 	ref = [[char_seg(s)] for s in ref_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]]
# 	hyp = double_emb_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]
# 	hyp = [char_seg(s) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating double embedding:")
# print ("character-based:")
# print ("neg sentences:")
# for i in range(len(words)):
# 	print (words[i]+' neg:', end='')
# 	ref = [[char_seg(s)] for s in ref_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]]
# 	hyp = double_emb_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]
# 	hyp = [char_seg(s) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating double embedding:")
# print ("segment-based:")
# print ("pos sentences:")
# for i in range(len(words)):
# 	print (words[i]+' pos:', end='')
# 	ref = [[list(jieba_seg(s))] for s in ref_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]]
# 	hyp = double_emb_pos[starting_index_pos[i]-1:starting_index_pos[i+1]-1]
# 	hyp = [list(jieba_seg(s)) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating double embedding:")
# print ("segment-based:")
# print ("neg sentences:")
# for i in range(len(words)):
# 	print (words[i]+' neg:', end='')
# 	ref = [[list(jieba_seg(s))] for s in ref_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]]
# 	hyp = double_emb_neg[starting_index_neg[i]-1:starting_index_neg[i+1]-1]
# 	hyp = [list(jieba_seg(s)) for s in hyp]
# 	print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

## Overall
# print ("evaluating double embedding:")
# print ("character-based:")
# print ("pos sentences:")
# ref = [[char_seg(s)] for s in ref_pos]
# hyp = double_emb_pos
# hyp = [char_seg(s) for s in hyp]
# print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating single embedding:")
# print ("character-based:")
# print ("pos sentences:")
# ref = [[char_seg(s)] for s in ref_pos]
# hyp = single_emb_pos
# hyp = [char_seg(s) for s in hyp]
# print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating double embedding:")
# print ("character-based:")
# print ("neg sentences:")
# ref = [[char_seg(s)] for s in ref_neg]
# hyp = double_emb_neg
# hyp = [char_seg(s) for s in hyp]
# print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

# print ("evaluating single embedding:")
# print ("character-based:")
# print ("neg sentences:")
# ref = [[char_seg(s)] for s in ref_neg]
# hyp = single_emb_neg
# hyp = [char_seg(s) for s in hyp]
# print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

ref_all = ref_pos + ref_neg 
old_all = single_emb_pos + single_emb_neg
new_all = double_emb_pos + double_emb_neg
print ("evaluating single embedding:")
print ("character-based:")
print ("all sentences:")
ref = [[char_seg(s)] for s in ref_all]
hyp = old_all
hyp = [char_seg(s) for s in hyp]
print (corpus_bleu(ref, hyp, smoothing_function=smoothie))

print ("evaluating double embedding:")
print ("character-based:")
print ("all sentences:")
ref = [[char_seg(s)] for s in ref_all]
hyp = new_all
hyp = [char_seg(s) for s in hyp]
print (corpus_bleu(ref, hyp, smoothing_function=smoothie))


# references = [[['this', 'is', 'a', 'test'], ['this', 'is' 'test']]]
# candidates = [['this', 'is', 'a', 'test']]
# score = corpus_bleu(references, candidates)
# print(score)






