
import pandas as pd
import csv

dat=pd.read_csv('human_sample_genes.csv')
#print(dat.head())

#Preprocessing data
id=dat.loc[:,'Promoter ID']
#print(id.head())

seq=dat.loc[:,'Sequence']
seq=list(seq)
print(seq)
