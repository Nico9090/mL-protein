#!/usr/bin/env python3
import requests
import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt
from collections import Counter
#____________________
#fetch sequences
def uniprotSQ(query,file):
        res=requests.get("https://rest.uniprot.org/uniprotkb/stream?query="+query)
        with open(file,"w")as store_file:
                store_file.write(res.text)
        return "Results stored"
#uniprotSQ("reviewed:true+go:*+length:[121+TO+121]&format=tsv&fields=accession,sequence,go_id","protSQLeq121.tsv")
#____________________
#read and pre-process
df = pd.read_csv("protSQLeq121.tsv", sep="\t")
#print(df.head(3))
#print("nrows: ",df.shape[0])
#print("ncol: ",df.shape[1])
#____________________
#GO term histogram
def go_hist(data_frame):
        go_terms=data_frame.iloc[:,-1] #last column is GO term
        go_terms=go_terms.str.split("; ")
        go_terms=list(chain.from_iterable(go_terms))
        counts=Counter(go_terms)
        data=pd.DataFrame(counts.items(),columns=["GO","count"])
        data=data.sort_values(by="count",ascending=False)
        plt_data=data.head(20)
        plt.figure(figsize=(12,6))
        plt.bar(plt_data["GO"],plt_data["count"])
        plt.xticks(rotation=45)
        plt.xlabel("GO term")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig("go_term_hist.png")
        plt.show()
        return "Histogram created!"
go_hist(df)
