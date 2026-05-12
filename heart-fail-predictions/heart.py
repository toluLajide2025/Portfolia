import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import file
df = pd.read_csv('C:/Users/lasel/Documents/Power BI/Heart failure/heart.csv')

# EDA

df.head()
df.info()

df['Age'].describe()
df['Age'].plot(kind='kde')

np.round(df['Sex'].value_counts(normalize=True) * 100, 2)
df['Sex'].value_counts().plot(kind='bar')
df['Sex'].value_counts().plot(kind='pie', legend=True)

df['ChestPainType'].value_counts()
df['ChestPainType'].value_counts().plot(kind='bar')
df[df['ChestPainType'] == 'NAP']

df.groupby(['ChestPainType'])['Sex'].value_counts().idxmax()
df[(df['ChestPainType'] == 'ASY') & (df['Age'] > 50)]
df.groupby(['ChestPainType'])['Age'].max()

df.groupby('Cholesterol')['RestingBP'].mean()
df[(df['ChestPainType'] == 'NAP') & (df['Age'] > 60) & (df['Sex'] == 'F')]
df.groupby(['ChestPainType', 'Sex'])['Age'].mean()

df.corr(numeric_only=True) 
df.isna().sum()
df.dropna(inplace=True)
df.rename(columns={'Sex':'Gender'}, inplace=True)
df[df.duplicated()]
df.drop_duplicates(inplace=True)
