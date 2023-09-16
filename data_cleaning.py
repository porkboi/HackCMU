# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1phTR_S7G0N4Iimq-rz5BWJ55nifQcwlc
"""

import os
import pandas as pd
import numpy as np
from sklearn import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pickle
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error


df = pd.read_csv("/path/to/src/exoplanetsdata.csv")
# link is: https://www.kaggle.com/datasets/maurobenjamin/exoplanets


# we don't care about these for now
# df2 = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/src/all_exoplanets_2021.csv")
# df3 = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/src/kepler.csv")

df_orig = df

bad_cols = ['disc_facility', 'facility_type', 'pl_controv_flag', 'disc_year', 'pl_controv_flag', "pl_insol", "pl_eqt", 'ttv_flag', 'pl_radj', 'pl_bmassj']
# remove: 'ra',
df_num = df.select_dtypes(exclude=['object'])
df_diff = df_num.loc[:, df_num.nunique() != 1]
df = df_diff.loc[:, ~df_diff.columns.isin(bad_cols)]
df = df.drop(columns = [col for col in df.columns if ('err' in col) or ('lim' in col)])
df = df.dropna()
df['hostname'] = df_orig['hostname']
df['hostname'] = df['hostname'].astype('category')
df['hostname_cat'] = df['hostname'].cat.codes
df['sy_pnum'].nunique()



X = df[["sy_snum", "pl_orbper", "pl_rade", "st_mass", "st_rad", "ra", "sy_dist", "sy_gaiamag", "pl_orbsmax", "sy_vmag", "sy_kmag"]]
y = df["st_met"]

while accuracy < 0.7:
  model = Sequential()
  model.add(Dense(250, input_shape=(12,), activation='relu'))
  model.add(Dense(750, activation='relu'))
  model.add(Dense(250, activation='relu'))
  model.add(Dense(8, activation='relu'))
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  model.fit(X, y, epochs=10, batch_size=50)
  _, accuracy = model.evaluate(X, y)
  print('Accuracy: %.2f' % (accuracy*100))

import tensorflow as tf
from sklearn.model_selection import train_test_split
from tabgan.sampler import OriginalGenerator, GANGenerator
X = df[["sy_snum", "pl_orbper", "pl_rade", "st_rad", "st_mass"]]
y = df["st_met"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
X_test.loc[len(df.index)] = [2, 5000, 1.5, 0.1, 1.8]
y_train = pd.DataFrame(y_train)
new_train1, new_target1 = OriginalGenerator().generate_data_pipe(X_train, y_train, X_test, )
#new_train2, new_target2 = GANGenerator().generate_data_pipe(X_train, y_train, X_test, )

X = df[["sy_snum", "pl_orbper", "pl_rade", "st_rad", "st_mass", "st_met"]]
y = df[["pl_bmasse"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
y_train = pd.DataFrame(y_train)
new_train2, new_target2 = OriginalGenerator().generate_data_pipe(X_train, y_train, X_test, )

X_train, X_test, y_train, y_test = train_test_split(new_train2, new_target2, test_size=0.05)

reg = make_pipeline(StandardScaler(),
                    SGDRegressor(max_iter=1000, tol=1e-3))
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
mean_squared_error(y_test, y_pred, squared=False)


filename = "planetMass.pickle"

pickle.dump(reg, open(filename, "wb"))

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(new_train1, new_target1, test_size=0.05)

knn = KNeighborsClassifier(n_neighbors=4073)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

ans = knn.predict([[2, 3, 1.5, 0.6, 1.8]])
print(ans)

X_train, X_test, y_train, y_test = train_test_split(new_train1, new_target1, test_size=0.05)

reg = make_pipeline(StandardScaler(),
                    SGDRegressor(max_iter=1000, tol=1e-3))
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
mean_squared_error(y_test, y_pred)

filename = "stellarM.pickle"

pickle.dump(reg, open(filename, "wb"))

X = pd.DataFrame(np.array([[2, 3, 1.5, 0.6, 1.8]]),
                   columns=["sy_snum", "pl_orbper", "pl_rade", "st_rad", "st_mass"])
