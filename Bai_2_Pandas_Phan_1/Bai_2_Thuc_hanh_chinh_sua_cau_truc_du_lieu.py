import numpy as np
import pandas as pd

df = pd.read_csv('assets/Food.csv')

# Đổi tên cột
df.rename(columns={'Place':'Vitri', 'Name':'TenSP'}, inplace=True)
print(df.columns);

# Thêm cột với giá trị mặc định
df['NYcu'] = 'Hoa';
print(df.head())

# Thêm cột mới từ một series
df['Sale'] = pd.Series('10%', index=df.index)
print(df.head())

# Thêm cột bằng lệnh insert(vị trí, tên cột mới, giá trị, )
df.insert(10, 'BigSale', '12%')
print(df.head())

# Xóa cột dùng lệnh del
del df['BigSale']
print(df.head())

# Xóa cột dùng lệnh pop
df.pop('NYcu')
print(df.head())

# Xóa 1 cột bằng lệnh drop
df.drop('Sale', axis=1, inplace=True)
print(df.head())

# Xóa nhiều cột bằng drop
df.drop(['Month', 'Year'], axis=1, inplace=True)
print(df.head())

# Xóa 1 dòng bằng drop theo index
df.drop(1, axis=0, inplace=True)
print(df.head())

# Xóa nhiều dòng bằng drop theo index (xóa dòng và không đổi index)
df.drop([2,3], inplace=True)
print(df.head())
