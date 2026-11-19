import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')

x=df['timestamp']
y=df['value']
plt.plot(x,y,marker='o',color='blue')
plt.title('my frist data plot')
plt.xlabel('timestamp')
plt.ylabel('value')
plt.show()