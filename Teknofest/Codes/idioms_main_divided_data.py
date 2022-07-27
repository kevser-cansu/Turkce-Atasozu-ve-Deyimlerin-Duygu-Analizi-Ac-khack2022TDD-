import pandas as pd
# import nltk
# import numpy as np

# from TurkishStemmer import TurkishStemmer
# stemmer = TurkishStemmer()
# stemmer.stem("okuldakilerden")


#Getting the data
idioms_data = pd.read_csv(r'Data\idioms_ten_created.csv')
ten_train = idioms_data.iloc[:,2]

from sklearn.feature_extraction.text import CountVectorizer

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VECTORIZER_1
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(ten_train)
print(ten_train)
print(vectorizer.get_feature_names_out())
print(X.toarray())

##checking the vocabulary/////////prints the positions in the sparse vector not the frequency
#print(vectorizer.vocabulary_)

# print('The length of vocabulary', len(vectorizer.get_feature_names()))

#Shape returned (9,48) means 9 rows(sentences) and 48 columns(unique words)
# print('The shape is', X.shape)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VECTORIZER_2
# vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2)) #only bigrams, (1,2) both unigrams and bigrams
# X2 = vectorizer2.fit_transform(ten_train),
# print(ten_train)
# print(vectorizer2.get_feature_names_out())
# print(X2.toarray())

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////VECTORIZER_TF_IDF
# from sklearn.feature_extraction.text import TfidfVectorizer
# #pass the stop words with the "stop_words=['the','we','should','this','to']" parameter manually or with a predefined list
# #max_df: float in range [0.0, 1.0] or int, default=1.0 ////// min_df: float in range [0.0, 1.0] or int, default=1
# tfidf_vectorizer = TfidfVectorizer()
# tfidf_df = tfidf_vectorizer.fit_transform(ten_train)
# print(ten_train)
# print(tfidf_vectorizer.get_feature_names_out())
# #print(tfidf_vectorizer.get_stop_words())
# print(tfidf_df.toarray())

