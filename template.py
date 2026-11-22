import pandas as pd

try:
    df=pd.read_csv('data.csv')
    print('成功读取数据')
    print(df.head())
    y =df['value']
    print('平均值是;',round(y.mean(),2))
except FileNotFoundError:
    print('电脑没有找到这个文件')