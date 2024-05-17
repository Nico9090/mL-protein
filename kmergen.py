#!/usr/bin/env python3

seq='ATCGTGATCT'
subgrp=int(input('How many chunks? '))
def kmer_gen(seq):
        k=[]
        for i in range(0,len(seq)-1):
                k.append(seq[i:i+subgrp])
        return k
print(kmer_gen('ATCGTGATCT'))
