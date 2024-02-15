#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#%%
iris = sns.load_dataset('iris')

# %%
print(iris.head())
print(iris.info())
print(iris.describe())


# %%
sns.pairplot(iris, hue='species')
plt.show()

# %%

X = iris.drop('species', axis=1)
y = iris['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
