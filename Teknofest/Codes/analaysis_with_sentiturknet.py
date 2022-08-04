import pandas as pd
import random
from spacy.tokenizer import Tokenizer
from spacy.lang.tr import Turkish
import numpy as np

nlp = Turkish()
stn_path = 'SentiTurkNet/STN.xlsx'
# train_path = '../Boun Twitter Data/train.json'
# val_path = '../Boun Twitter Data/validation.json'
# test_path = '../Boun Twitter Data/test.json'

stn = pd.read_excel(stn_path)

stn = stn.drop_duplicates(['synonyms']).set_index('synonyms')
final_stn = {}
for words in stn.index:
    if words is np.nan:
        continue
    for word in words.split(','):
        final_stn[word.strip()] = {'pos':stn.loc[words]['pos value'],'neg':stn.loc[words]['neg value']}
        
def feature_extraction(text):
    pos_val = 0
    neg_val = 0 
    for token in nlp(text):#splitting sentence into words by nlp(text)
        word = token.text.lower()
        if word in final_stn:
            pos_val+=final_stn[word]['pos']
            neg_val+=final_stn[word]['neg']
    return [pos_val, neg_val]


idiom_1 = "Herhangi bir işteki eksiği, hileyi veya zararı ortaya çıkarmak"
print(feature_extraction(idiom_1))