# Source:
# https://chrisalbon.com/machine_learning/trees_and_forests/random_forest_classifier_example/

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

iris = load_iris()
print(len(iris['data']), iris)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# seperate into training and testing set, 3:1
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
# https://stackoverflow.com/questions/21689423/pandas-attribute-error-no-attribute-factor-found
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.head()

train, test = df[df['is_train']==True], df[df['is_train']==False]

features = df.columns[:4]
clf = RandomForestClassifier(n_jobs=3)
# factorize enumerates each species with a unique numerical id
y, _ = pd.factorize(train['species'])
clf.fit(train[features], y)

# do predictions
preds = iris.target_names[clf.predict(test[features])]
print(preds)

# confusion matrix
pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])