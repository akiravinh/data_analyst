# %%
import numpy as np
import pandas as pd

# Đọc dữ liệu từ file csv
df = pd.read_csv('assets/FoodPrice_in_Turkey.csv')
print(df.head(5))