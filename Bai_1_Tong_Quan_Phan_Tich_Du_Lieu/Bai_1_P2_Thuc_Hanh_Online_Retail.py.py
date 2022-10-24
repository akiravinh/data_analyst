# %%
import numpy as np
import pandas as pd

df = pd.read_csv('./Retail2.csv', encoding='utf-8')
df['Total'] = df['Quantity'] * df['UnitPrice']
print('Tổng số đơn hàng bán :', df.Quantity.sum())
print('Tổng giá trị đơn hàng bán :', df.Total.sum(), 'USD')
print('Tổng số các nước được pp :', df.Country.unique().size)
print('*'*30)
print('Mặt hàng có doanh số lớn nhất :')
df2 = df[['StockCode', 'Description', 'Quantity']].sort_values('Quantity', ascending=False)
print(df2.head(10))
print('*'*30)
print('Mặt hàng có doanh thu lớn nhất :')
df3 = df[['StockCode', 'Description', 'Quantity', 'Total']
         ].sort_values('Total', ascending=False)
print(df3.head(10))
# %%
