import pandas as pd
import matplotlib.pyplot as plt

c=pd.read_csv('./cancer.csv')
c=pd.DataFrame(c)
print(c.isna().sum())
c=c.dropna(axis=0, how='any')

c.boxplot()
plt.show()

