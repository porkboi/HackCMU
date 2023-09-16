import pickle
#from sklearn.linear_model import SGDRegressor
from sklearn import *
import pandas as pd
import numpy as np
### This interfaces the model with the frontend ###

df = pd.read_csv("src\exoplanetsdata.csv")

def locate_star(pred_met):
    idx = abs(df['st_met'] - pred_met).idxmin()
    return df.at[idx, 'hostname']

def model_stellarM(lst):
    loaded_model = pickle.load(open("stellarM.pickle", "rb"))
    #tuples = list(zip(lst, ["sy_snum", "pl_orbper", "pl_rade", "st_rad", "st_mass"]))
    X = pd.DataFrame(np.array([lst]),
                     columns=["sy_snum", "pl_orbper", "pl_rade", "st_rad", "st_mass"])
    #print(X)
    y = loaded_model.predict(X)
    return y[0]

def model_planetMass(lst):
    loaded_model = pickle.load(open("planetMass.pickle", "rb"))
    X = pd.DataFrame(np.array([lst]),
                     columns=["sy_snum", "pl_orbper", "pl_rade", "st_rad", "st_mass", "st_met"])
    y = loaded_model.predict(X)
    return y[0]

#print(model_planetMass([2, 5000, 1.5, 0.1, 1.8, 0.14165]))