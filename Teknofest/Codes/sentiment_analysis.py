import pandas as pd
import numpy as np

data_idioms = pd.read_csv('Data\idioms_translation_2.csv', delimiter=';' )
# print(data_idioms.head())
idiom_translation = data_idioms.iloc[:,2]
# print(idiom_translation)

from sentistrength import PySentiStr
senti = PySentiStr()
senti.setSentiStrengthPath('C:/Users/Kevser Cansu/Documents/SentiStrength.jar') # Note: Provide absolute path instead of relative path
senti.setSentiStrengthLanguageFolderPath('C:/Users/Kevser Cansu/Documents/SentStrength_Data_Sept2011') # Note: Provide absolute path instead of relative path

#Scale Score
new_list_scale = []
for i in range(len(idiom_translation)):
    new_list_scale.append(*senti.getSentiment(idiom_translation[i], score='scale'))
    # print(*senti.getSentiment(idiom_translation[i], score='scale'))

# print(new_list_scale)    
df_list_scale = pd.DataFrame(new_list_scale)

#dual scoring (a score each for positive rating and negative rating)
new_list_dual = []
for i in range(len(idiom_translation)):
    new_list_dual.append(*senti.getSentiment(idiom_translation[i], score='dual'))
    # print(*senti.getSentiment(idiom_translation[i], score='dual'))
df_list_dual = pd.DataFrame(new_list_dual)

#trinary scoring (a score each for positive rating, negative rating and neutral rating)
new_list_trinary = []
for i in range(len(idiom_translation)):
    new_list_trinary.append(*senti.getSentiment(idiom_translation[i], score='trinary'))
    # print(*senti.getSentiment(idiom_translation[i], score='trinary'))
    
df_list_trinary = pd.DataFrame(new_list_trinary)

#binary scoring (1 for positive sentence, -1 for negative sentence)
new_list_binary = []
for i in range(len(idiom_translation)):
    new_list_binary.append(*senti.getSentiment(idiom_translation[i], score='binary'))
    # print(*senti.getSentiment(idiom_translation[i], score='binary'))
df_list_binary = pd.DataFrame(new_list_binary)

result = pd.concat((idiom_translation, df_list_scale), axis=1)
result_1 = pd.concat((result, df_list_dual), axis=1)
result_2 = pd.concat((result_1, df_list_trinary), axis=1)
result_3 = pd.concat((result_2, df_list_binary), axis=1)
# result_3.columns['İngilizce Anlamı', 'Scale Score', 'Dual Score POS', 'Dual Score NEG', 'Trinary Score POS', 'Trinary Score NEG', 'Trinary Score NEUT', 'Binary Score']
last_df = pd.concat((data_idioms, result_3), axis=1)
# print(result_3.head())
last_df.to_excel('Data\idioms_with_sentiment_scores_original.xlsx')