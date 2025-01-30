#!/usr/bin/env python3
nucl_dict={"A":"T","C":"G","T":"A","G":"C"}
seq="AgACTCATCTCATTCCACgAAgCTATTTACATACACCTTgTCgCTgACTCCC"
seq=seq.upper()
complement=[]
for nucleotide in seq:
        complement.append(nucl_dict[nucleotide])
complement=''.join(complement)
print(complement)
