# %%
# Thực hành GDP
import numpy as np
import pandas as pd

# Đọc file
df = pd.read_csv('./assets/GDPlist.csv', encoding='iso-8859-1')

# Thông tin số dòng và số cột
print(f'Số dòng : {df.shape[0]} và số cột : {df.shape[1]} \n')

# GDP các nước có đều không ?
print('GDP các nước có đều nhau không')
print('STD =', df.GDP.std())

# Mỗi châu lục có bao nhiêu nước
print('\n Mỗi châu lục có bao nhiêu nước')
print(df.groupby('Continent')['Country'].count())

# GDP của các châu lục
print('\n GDP của các châu lục là :')
print(df[['Continent', 'Country', 'GDP']].groupby('Continent').sum())

# Top 10 nước có GDP cao nhất
print('\n Top 10 nước có GDP cao nhất là :')
print(df.sort_values('GDP', ascending=False).head(10))

