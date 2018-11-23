# SD_translation

This repo is for my project: Sentiment Disambiguation for English to Chinese Machine Translation.

This project is for Google Science Fair Submission. We are still working to further improve it to an NAACL submission.

I did not have the time to clean it up and make it more user friendly yet, but you should be able to use the codes to reproduce all the 
experiments and evaluation.

I am using a very simple seq2seq for NMT without tuning hyperparameters, you should try to use more advanced architectures (attention, Transformer, etc) and train for 
more epochs to get even better results (the BLEU scores in my experiments are actually very low). 
NMT tensorflow implementation reference: https://github.com/caicloud/tensorflow-tutorial/tree/master/Deep_Learning_with_TensorFlow/1.4.0/Chapter09

Please feel free to contact me (sichenglei1125@gmail.com) if you have any question.

I might add a detailed explanation of the codes later, but for now you can refer to the comments in the codes.

The key novelty between my model and convental NMT systems is that I am using double word vectors for ambiguous words. I did this by treating the positive sentiment and negative sentiment of the ambiguous word as two different words. That's why there is a python script in the corpus directory that changes the negative sentiment of the word to 'word_neg'. (Positive sentiments remain the original form.) They are treated as different words and have different word indices in the vocabulary and have different embedding vectors.
