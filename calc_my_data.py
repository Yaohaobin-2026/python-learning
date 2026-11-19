import pandas as pd
print("---准备读取我自己创造的数据---")
df=pd.read_csv('data.csv')

print("\n---数据长这样---")
print(df)

print("\n---开始计算---")
avg_val=df['value'].mean()
max_val=df['value'].max()
min_val=df['value'].min()

print(f'这8个数的平均值是:{avg_val}')
print(f'最大值是：{max_val}')
print(f'最小值是：{min_val}')
