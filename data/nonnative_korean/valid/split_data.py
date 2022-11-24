import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('4.csv')
print(df)
train, test = train_test_split(df, test_size=0.5, random_state=42, shuffle=True)

train.to_csv('../test/4.csv', index=False)
