pip install pandas
pip install numpy

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


df = pd.DataFrame({
    'Date': ['2023-01-01', '02-01-2023', 'Invalid'],
    'Category': ['Apple', 'apple', 'Banana'],
    'Value': [10, 1500, 20],
    'Missing': [1, np.nan, 3]
})

print("Original Data:\n", df)


df.drop_duplicates(inplace=True)


df['Missing'] = df['Missing'].fillna(df['Missing'].mean())


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df['Date'] = df['Date'].ffill()


df['Category'] = df['Category'].str.lower()

df['Value'] = df['Value'].clip(upper=100)


scaler = MinMaxScaler()
df['Value_norm'] = scaler.fit_transform(df[['Value']])

print("\nCleaned Data:\n", df)

