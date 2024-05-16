#!/usr/bin/env python3

#Obtaining the file
with open('sample_DNA.txt','r')as f:
        sequence=''
        for line in f:
                sequence+=line
        sequence=sequence.rstrip('\n')
length=0
for base in sequence:
        length+=1

#Get number of groups
k=int(input('How many groups of subsequences do you want from the chosen DNA sequence? '))
km=length-k+1

#Get number of individual bases(kmers)
bases=4**k
print('The number of subsequences you have chosen is ',km)
print('The number of bases present is ',bases)
