import pandas as pd
import numpy as np
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

data_idioms = pd.read_csv('Data\idioms_translation_2.csv', delimiter=';' )
# print(data_idioms.head())
idiom_translation = data_idioms.iloc[0:9,2]
# print(idiom_translation)


#removing stopwords from sentences, words or tokens(?) 