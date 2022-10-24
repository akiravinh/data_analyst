# %%
# Jupyter notebook được cài trong VScode @vinhhd68@gmail.com

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('assets/covid.csv') # Đọc file
f2 = data[data.date == '12/04/2020'] # Lựa chọn data chính của file là dữ liệu ngày 12/4/2020
print(f2.groupby('continent')['cases','deaths'].sum()) # Phân loại theo group là các châu lục trên thế giới
f3 = f2.sort_values('cases', ascending=False) # Sắp xếp các nước có số ca nhiễm covid cao nhất
print(f3)
table1 = plt.hist(f2.cases, bins=200) # Bảng dữ liệu về số ca nhiễm của các nước
table1


# %%
