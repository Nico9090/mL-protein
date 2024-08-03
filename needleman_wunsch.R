#Needleman Wunsch 

#Setting values for match, mismatch, and gap
match <- 1
mismatch<- -1
gap <- -1

#Setting the two sequences
seq1<- "ATCGAT"
seq2<- "TTACAT"

#Score matrix

score_matrix<- matrix(nrow = nchar(seq1)+1, ncol = nchar(seq2)+1)
#print(paste("SCORE MATRIX:")) 
#print(score_matrix)

score_matrix[1,2]= "A"
i<-2
j<-1
s<-1
while (i<=nchar(seq1) & j == 1){
  score_matrix[j,i]=seq1[s]
  i=i+1
  s=s+1
  if (i == nchar(seq1)){
    j <- j+1
    i <- 1
    s <- 1
    while(j<=nchar(seq2)){
      score_matrix[j,i]=seq2[1]
      j=j+1
      s=s+1
    }
  }
}
