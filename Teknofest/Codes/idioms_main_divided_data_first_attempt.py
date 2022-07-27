import pandas as pd
import nltk
# import numpy as np

#Getting the data
idioms_data = pd.read_csv(r'Data\idioms_ten_created.csv')
# print(idioms_data.iloc[:,2:3])

# Sample sentences.
# sentences = idioms_data.iloc[:,2:3]
# # [
#     "This is a sample sentence",
#     "I am interested in politics",
#     "You are a very good software engineer, engineer.",
# ]

# Create CountVectorizer, which create bag-of-words model.
# stop_words : Specify language to remove stopwords. 
# vectorizer = CountVectorizer(encoding="utf-8")
# type(vectorizer)
# # Learn vocabulary in sentences. 
# vectorizer.fit(sentences)

# # Get dictionary. 
# print(vectorizer.get_feature_names_out())

ten_train = idioms_data.iloc[:,1]
# print(ten_train)


from sklearn.feature_extraction.text import CountVectorizer
# count_vect = CountVectorizer()
# X_train_counts = count_vect.fit_transform(ten_train)

# df2 = pd.DataFrame(X_train_counts.toarray().transpose(), index=count_vect.get_feature_names_out())

# df2.columns = ten_train.columns
# print(df2)


# corpus = [
#     'This is the first document.',
#     'This document is the second document.',
#     'And this is the third one.',
#     'Is this the first document?',
# ]
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(ten_train)
# print(ten_train)
# print(vectorizer.get_feature_names_out())
# print(X.toarray())

vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
X2 = vectorizer2.fit_transform(ten_train)
print(ten_train)
print(vectorizer2.get_feature_names_out())
print(X2.toarray())


