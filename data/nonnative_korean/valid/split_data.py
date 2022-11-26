import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('4_valid.csv')
print(df)
train, test = train_test_split(df, test_size=0.5, random_state=42, shuffle=True)

test.to_csv('4.csv', index=False)
train.to_csv('../../test/less_17/4.csv', index=False)
