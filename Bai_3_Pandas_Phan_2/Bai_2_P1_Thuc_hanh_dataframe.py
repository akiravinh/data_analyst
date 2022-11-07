# %%
import numpy as np
import pandas as pd

# Đọc dữ liệu từ file csv
df = pd.read_csv('assets/FoodPrice_in_Turkey.csv')
df.to_csv('assets/FoodPrice_in_Turkey_export.csv')
print('Xuất file output thành công')