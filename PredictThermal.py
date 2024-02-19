# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:03:19 2023

@author: Surjeet
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:00:17 2023

@author: Surjeet
"""


"""
"""
import pandas as pd
import numpy as np


from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import cross_val_score


from sklearn.model_selection import KFold
import seaborn as sns
import matplotlib.pylab as plt
from sklearn.feature_selection import VarianceThreshold




data = pd.read_csv("ICSD_stability.csv")
data = data.dropna()


X = data.drop("filename", axis = 1)
X = X.drop("mat", axis = 1)
X = X.drop("stability", axis = 1)



inputs = X



import pickle

loaded_model = pickle.load(open("Extra_Trees.sav", 'rb'))
result = loaded_model.predict(inputs)
print(result)

