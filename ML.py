#!/usr/bin/env python3
import requests
import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.preprocessing import MultiLabelBinarizer

mL_df=pd.read_csv("mouse_prot_MLin.csv",sep="\t")
print(mL_df.columns)
#Training the model___________________________________
X_train,Y_train=mL_df['sequence matrix'],mL_df['multi-hit GO']

