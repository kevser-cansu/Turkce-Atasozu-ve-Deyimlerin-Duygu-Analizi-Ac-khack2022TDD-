import pandas as pd

synset = pd.read_excel(r"SentiTurkNet\STN.xlsx")
idioms_data = pd.read_csv(r'Data\idioms_ten_created.csv')

synset_data = synset.loc[:,['synonyms','neg value','obj value', "pos value"]]

# print(idioms_data.head())
# print(synset_data.head())

sentence = "Herhangi bir işteki eksiği, hileyi veya zararı ortaya çıkarmak"
from nltk import word_tokenize

#TOKENLARA AYIRMA
words = word_tokenize(sentence, "turkish")

#NOKTALAMA İŞARETLERİNİ KALDIRMA
new_words = [word for word in words if word.isalnum()]

import zeyrek
analyzer = zeyrek.MorphAnalyzer()

#TÜRKÇE LEMMATIZATION
tokens_and_lemmas = [analyzer.lemmatize(i) for i in new_words]

new_list = []
for i in range(len(tokens_and_lemmas)):
    new_list.append(tokens_and_lemmas[i][0][1])    
# print(new_list)

#DATA FRAME'E ÇEVİRME
df_lemmas = pd.DataFrame(new_list)
# print(df_lemmas)

print(new_list)

for i in range(len(df_lemmas)):
    subset_df = synset_data.loc[synset_data['synonyms'] == df_lemmas.iloc[i,0]]

print(subset_df)
