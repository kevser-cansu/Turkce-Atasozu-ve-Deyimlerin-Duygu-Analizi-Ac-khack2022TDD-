import pandas as pd

labeled_data = pd.read_csv('Data\idioms_with_sentiment_scores.csv', delimiter=';' )
# print(labeled_data.info())
labeled = labeled_data.iloc[:,10]
# print(labeled.head())

ct_p = 0
ct_n = 0
for i in range(len(labeled_data)):
    if labeled_data.iloc[i,10] == 'P':
        # final_labels.append()
        ct_p += 1
    elif labeled_data.iloc[i,10] == 'N':
        ct_n += 1

print(ct_p)
print(ct_n)

finals = labeled_data.loc[labeled_data['Duygu (Pozitif, Negatif)'].isin(['N', 'P'])]

print(finals.head())
print(len(finals))

# finals.to_csv(r'D:\Teknofest\Data\final_labeled.csv')
# finals.to_excel(r'D:\Teknofest\Data\final_labeled.xlsx')