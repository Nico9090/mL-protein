#!/usr/bin/env python3
import requests
import pandas as pd
from itertools import chain
import matplotlib.pyplot as plt
from collections import Counter

url="https://rest.uniprot.org/uniprotkb/stream?query=reviewed:true+go:*+organism_id:10090&format=tsv&fields=accession,sequence,go_id"
res=requests.get(url)
with open("mouse_go.tsv","w")as outfile:
        outfile.write(res.text)

df = pd.read_csv("mouse_go.tsv", sep="\t")
#print("nrows: ",df.shape[0])
#print("ncol: ",df.shape[1])

#GO term histogram

go_terms=df.iloc[:,-1]
hx=go_terms.str.split('; ')
hx=list(chain.from_iterable(hx))
with open("mouse_gterms.txt","w")as hist_file:
        for term in hx:
                hist_file.write(term + "\n")


counts=Counter(hx)
data=pd.DataFrame(counts.items(),columns=["GO","count"])

data=data.sort_values(by="count",ascending=False)
plt_data=data.head(20)

#plot
plt.figure(figsize=(12,6))
plt.bar(plt_data["GO"],plt_data["count"])
plt.xticks(rotation=45)
plt.xlabel("GO term")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("go_term_hist.png")
plt.show()
