import csv
import pandas as pd

df = pd.read_csv('employees.csv', usecols=['name','email','department']).drop_duplicates(keep='first').reset_index()
# df['email'].fillna('dummy@email.com', inplace=True)
df['email'] = df['email'].fillna('dummy@example.com')
df.to_csv('out_file.csv', index=False)