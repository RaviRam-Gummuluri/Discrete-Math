#Roll 211AI018 : Discrete Math Lab 2
#Name-Gummuluri Venkata Ravi Ram
#NITK, SURATHKAL

import ttg
import pandas as pd

#creating file name for output as per test case.
t=input('Enter the test case number : ')
fname='OUTPUT_TC'+t+'.txt'

#taking boolean statement as input in form of string
#the literals used must have blank space on both sides of it to get recognized as literal 
str=input('Enter the boolean statement : ')
arr=str.split() 
parr=[]
for alpha in arr:
    if alpha in list(map(chr,range(97,123))):
        parr.append(alpha)

#identified literals used in given statement and stored in parr
parr=list(set(parr))
parr.sort()
print(parr)

#creating truth table
booleval=(ttg.Truths(parr,[str]))
df = pd.DataFrame(booleval.as_pandas()).to_numpy()

#inferencing DNF from truth table
result ='DNF of given boolean statement is '
for i in range(0 , int(2**len(parr))):
    if(df[i][len(parr)] == 1):
        result += '( '
        for j in range(len(parr)-1):
            if df[i][j]==1:
                result += parr[j]+' ^ '
            else:
                result += '~'+parr[j]+' ^ '
        if df[i][len(parr)-1]==1:
            result += parr[len(parr)-1]
        else:
            result += '~'+parr[len(parr)-1]
        result += ' ) v '

#opening file and prnting output onto file as well as console
with open(fname,'w') as file:
    print(booleval,file=file)
    print(booleval)
    print(result[0:len(result) - 2],file=file)
    print(result[0:len(result) - 2])
file.close()

