import pandas as pd
import numpy as np

data = pd.read_csv("data/202010.csv")
nodelist = data["시점명"].unique()
print(nodelist)
nodedict = {}
for idx, name in enumerate(nodelist):
    nodedict[idx] = name
print(nodedict)