from sklearn.datasets import load_wine
import pandas as pd 
import mglearn 
import matplotlib.pyplot as plt

data = load_wine()
print(data["data"])
data_df = pd.DataFrame(data["data"])

pd.plotting.scatter_matrix(data_df, c=data["target"], figsize=(15, 15), marker='o',
                           hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
plt.show()