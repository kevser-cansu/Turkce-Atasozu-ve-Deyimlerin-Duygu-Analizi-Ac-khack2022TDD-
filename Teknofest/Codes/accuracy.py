import pandas as pd

label_data = pd.read_csv(r'Data\final_labeled.csv')
# print(label_data.head())
print(label_data.info())


ct_true = 0
ct_false = 0
for i in range(len(label_data)):
    if label_data.iloc[i,11] == 'N' and label_data.iloc[i,4] < 0:
    # if label_data.iloc[i,11] == 'N' and float(label_data.iloc[i,5]) + float(label_data.iloc[i,6]) < 0:
        ct_true += 1
    elif label_data.iloc[i,11] == 'P' and label_data.iloc[i,4] > 0:
    # elif label_data.iloc[i,11] == 'P' and float(label_data.iloc[i,5]) + float(label_data.iloc[i,6]) > 0:
        ct_true += 1
    elif label_data.iloc[i,11] == 'P' and label_data.iloc[i,4] < 0:
    # elif label_data.iloc[i,11] == 'P' and float(label_data.iloc[i,5]) + float(label_data.iloc[i,6]) < 0:
        ct_false += 1
    elif label_data.iloc[i,11] == 'N' and label_data.iloc[i,4] > 0:
    # elif label_data.iloc[i,11] == 'N' and float(label_data.iloc[i,5]) + float(label_data.iloc[i,6]) > 0:
        ct_false += 1
    
print(ct_true)
print(ct_false)

sum = ct_true + ct_false
t_rate = ct_true / sum
print('Accuracy rate: ',float(t_rate))