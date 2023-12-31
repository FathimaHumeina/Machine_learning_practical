# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SroP8jXnMhukjK6sRxocJWfeRXMC9f86
"""

import pandas as pd

df=pd.DataFrame({
    'area':[2600,3000,3200,3600,4000],
    'price':[550000,565000,610000,680000,725000]
})



df

from sklearn import linear_model
reg=linear_model.LinearRegression()

x=df['area']
y=df['price']

reg.fit(df[['area']],df['price'])

reg.intercept_

reg.coef_

reg.predict([[8000]])

import matplotlib.pyplot as plt

plt.scatter(df['area'],df['price'])

import pickle

with open('model_pickle','wb') as f:
  pickle.dump(reg,f)

with open('model_pickle','rb') as f:
  mp=pickle.load(f)

mp.predict([[8000]])

import pickle

df=pd.DataFrame({
    'area':[2600,3000,3200,3600,4000],
    'price':[550000,565000,610000,680000,725000]
})

from sklearn import linear_model

reg=linear_model.LinearRegression()

reg.fit(df[['area']],df['price'])

with open('pickle_model','wb') as f:
  pickle.dump(reg,f)

with open('pickle_model','rb') as f:
  mp=pickle.load(f)

mp.predict([[8000]])

pip install joblib

import joblib

joblib.dump(reg,'model_joblib')

model=joblib.load('model_joblib')

model.predict([[8000]])

