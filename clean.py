#!/usr/bin/env python3
import requests
import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt
from collections import Counter

#_____________________________________
df=pd.read_csv("mouse_go.tsv",sep="\t")
print(df.head(3))

#Filtering____________________________
#print(df.isna().any().any())
go_terms=df.iloc[:,-1]
go_terms=go_terms.str.split('; ')
go_terms=list(chain.from_iterable(go_terms))

counts=Counter(go_terms)
data=pd.DataFrame(counts.items(),columns=["GO","count"])
print("unfiltered sequence collection: ",data.shape[0])
filt_count=data[data["count"]>10]
print("filtered sequence collection: ",filt_count.shape[0])
