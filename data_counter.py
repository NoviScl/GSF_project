#count the avg length of input/output sentence 
TED = "datasets/TED/"
EN_DATA = [TED+"train_nosp_idx.en", "datasets/new_train_sp_idx.en"]
ZH_DATA = [TED+"train_nosp_idx.zh", "datasets/share_train_sp_idx.zh"]

for data in EN_DATA:
	len_sum = 0
	len_num = 0
	with open(data, 'r') as f:
		flines = f.readlines()
		len_sum += sum([len(line.strip().split()) for line in flines])
		len_num += len(flines)
print ("eng data: ", len_sum/len_num)


for data in ZH_DATA:
	len_sum = 0
	len_num = 0
	with open(data, 'r') as f:
		flines = f.readlines()
		len_sum += sum([len(line.strip().split()) for line in flines])
		len_num += len(flines)
print ("zh data: ", len_sum/len_num)

#EN: 50
#ZH: 49.7

#set MAX_LEN = 50 for both en and zh

