#Roll 211AI018 : Discrete Math Lab 3
#Name-Gummuluri Venkata Ravi Ram
#NITK, SURATHKAL

import ttg

#creating output file based on test case number
t=input('Enter the test case number : ')
fname='OUTPUT_TC'+t+'.txt'
file=open(fname,'w')

#taking inputs
in1=input('Enter premise 1 : ')
in2=input('Enter premise 2 : ')
in3=input('Enter Inference : ')
in4='('+in1+') and ('+in2+')'
in5='(('+in1+') and ('+in2+'))'+' => '+'('+in3+')'

#converting inputted strings into list of words
parr=[]
arr1=in1.split()
arr2=in2.split()
arr3=in3.split()

#identifying literals
for alpha in arr1:
    if alpha in list(map(chr,range(97,123))):
        parr.append(alpha)
for alpha in arr2:
    if alpha in list(map(chr,range(97,123))):
        parr.append(alpha)
for alpha in arr3:
    if alpha in list(map(chr,range(97,123))):
        parr.append(alpha)

parr=list(set(parr))
parr.sort()

#drawing truth table
booleval=(ttg.Truths(parr,[in1,in2,in3,in4,in5]))
print(booleval,file=file)
print(booleval)


