#tokenize english data
#perl ./tokenizer.perl -no-escape -l "en" < ../datasets/TED/train.raw.en > ../datasets/TED/train.txt.en 
#perl ./tokenizer.perl -no-escape -l "en" < ../datasets/UN/MultiUN.en > ../datasets/UN/UN_seg.en 
perl ./tokenizer.perl -no-escape -l "en" < ../datasets/special_words/test_neg.en > ../datasets/special_words/test_neg_seg.en 
perl ./tokenizer.perl -no-escape -l "en" < ../datasets/special_words/test_pos.en > ../datasets/special_words/test_pos_seg.en 
perl ./tokenizer.perl -no-escape -l "en" < ../datasets/special_words/train_neg.en > ../datasets/special_words/train_neg_seg.en 
perl ./tokenizer.perl -no-escape -l "en" < ../datasets/special_words/train_pos.en > ../datasets/special_words/train_pos_seg.en 


#tokenizer chinese data
#sed 's/ //g; s/./& /g' ../datasets/TED/train.raw.zh > ../datasets/TED/train.txt.zh
#sed 's/ //g; s/./& /g' ../datasets/UN/MultiUN.zh > ../datasets/UN/UN_seg.zh
#sed 's/ //g; s/./& /g' ../datasets/aiChallenger/train.zh > ../datasets/aiChallenger/train_seg.zh
sed 's/ //g; s/./& /g' ../datasets/special_words/test_neg.zh > ../datasets/special_words/test_neg_seg.zh
sed 's/ //g; s/./& /g' ../datasets/special_words/test_pos.zh > ../datasets/special_words/test_pos_seg.zh
sed 's/ //g; s/./& /g' ../datasets/special_words/train_neg.zh > ../datasets/special_words/train_neg_seg.zh
sed 's/ //g; s/./& /g' ../datasets/special_words/train_pos.zh > ../datasets/special_words/train_pos_seg.zh





