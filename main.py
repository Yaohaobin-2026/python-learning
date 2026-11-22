import pandas as pd
df =pd.read_csv('data.csv')
print('成功读取数据')

print(df.head())

y=df['value']
print('平均值是:',round(y.mean(),2))
