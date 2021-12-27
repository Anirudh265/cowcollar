import pandas as pd
import matplotlib.pyplot as plt
#dataframe1 = pd.read_csv("cow_data.csv")
dataframe1.columns=['date','time','x','y','z']
print(dataframe1)
ax = plt.gca()
dataframe1.plot(kind='line', x='time', y='x', color='green', ax=ax)
dataframe1.plot(kind='line', x='time', y='y', color='red', ax=ax)
dataframe1.plot(kind='line', x='time', y='z', color='blue', ax=ax)
plt.show()
