# %%
import numpy as np
import pandas as pd

df = pd.read_csv('assets/FoodPrice_in_Turkey.csv')

# Đọc số dòng và số cột của bảng dữ liệu
print(f'Số dòng là : {df.shape[0]} và số cột là : {df.shape[1]}')

# Thang đo của các thuộc tính
print('Thang đo dữ liệu :')
print(df.info())

# Số loại thực phẩm được thống kê
print(f'\nSố loại thực phẩm trong danh sách : {df.ProductName.unique().size} \n')

# Giá trung bình của các loại thực phẩm
print('Giá trung bình của các loại thực phẩm là :')
print(df.groupby('ProductName')['Price'].mean())



# %%
