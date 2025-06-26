#!/usr/bin/env python3
import requests
import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.preprocessing import MultiLabelBinarizer
#from transformers import T5Tokenizer, T5EncoderModel
#import torch
import numpy as np
#_____________________________________
df=pd.read_csv("mouse_go.tsv",sep="\t")
#Filtering____________________________
go_terms=df.iloc[:,-1]
go_terms=go_terms.str.split('; ')
go_terms=list(chain.from_iterable(go_terms))
counts=Counter(go_terms)
data=pd.DataFrame(counts.items(),columns=["GO","count"])
filt_count=data[data["count"]>10]
#________________________________________
df2=df[df["Gene Ontology IDs"].isin(filt_count["GO"])] #use this
mlb = MultiLabelBinarizer()
Y = mlb.fit_transform(df2["Gene Ontology IDs"])
df2["multi-hit GO"]=[list(row) for row in Y] #converted each GO term in GO column to multi hit
#print(df2.iloc[0,1])
#_________________________________________
#Encode protein sequences
def prot_matrix(sequence):
        cols=["A","L","K","W","F","Y","G","D","N","C","T","V","M","R","I","S","P","H","E","Q"]
        rows=[i for i in sequence]
        df = pd.DataFrame(index=rows, columns=cols)
        for val in df.index:
                for let in df.columns:
                        if val==let:
                                df.loc[val,let]=1
                        else:
                                df.loc[val,let]=0
        return df
print(prot_matrix(df2.iloc[1,1]))
matrices=[]
step=0
while step<df2.shape[0]:
        matrices.append(prot_matrix(df2.iloc[step,1]))
        print("sequence ", step, " added!")
        step+=1
df2["sequence matrix"]=matrices
#print(df2.head(2))
df2.to_csv('mouse_prot_MLin.csv', sep='\t', index=False)

#_____________________________________________________________
#read ML model

"""tokenizer = T5Tokenizer.from_pretrained("Rostlab/prot_t5_xl_uniref50")
model = T5EncoderModel.from_pretrained("Rostlab/prot_t5_xl_uniref50")
model = model.eval()
#________________________________________
def embed_sequence(sequence):
    sequence = ' '.join(list(sequence))  # tokenize amino acids
    tokens = tokenizer(sequence, return_tensors="pt", padding=True)
    with torch.no_grad():
        embeddings = model(**tokens).last_hidden_state
    return embeddings.mean(dim=1).squeeze().numpy()
"""

