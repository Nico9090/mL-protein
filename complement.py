#!/usr/bin/env python3
with open('sample_DNA.txt','r')as f:
        sequence=''
        for line in f:
                sequence+=line
        sequence=sequence.rstrip('\n')
f.close()
base_dict={'A':'T','T':'A','G':'C','C':'G'}
compl=''
for base in sequence:
        compl+=base_dict[base]
f=open('DNA_compl.txt','w')
print(sequence,file=f)
print(compl,file=f)
f.close()
