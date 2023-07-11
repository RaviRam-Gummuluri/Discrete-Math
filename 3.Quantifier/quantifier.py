#Roll 211AI018 : Discrete Math Lab 2
#Name-Gummuluri Venkata Ravi Ram
#NITK, SURATHKAL

t=input('Enter the test case number : ')
fname='OUTPUT_TC'+t+'.txt'
file=open(fname,'w')

print("(Use there_exists for 'there exists' and for _all for 'for all')")
stri=input("Enter the propositional statement : ")
print('\n')
supp=['(P','(~P']
sign=[' v ',' ^ ']
if 'there_exists' in stri:
    arr=stri.split('there_exists')
    ci=arr[0].count('~')
    ca=arr[1].count('~')
    p='there_exists'
    q=0
elif 'for_all' in stri:
    arr=stri.split('for_all')
    ci=arr[0].count('~')
    ca=arr[1].count('~')
    p='for_all'
    q=1

s=1

print(' Ques : '+stri)
print(' Ques : '+stri,file=file)
if ci>1 or ca>1:
    print('Step '+str(s)+': ',end='')
    print('Step '+str(s)+': ',end='',file=file)
    if ci%2!=0:
        print('~',end='')
        print('~',end='',file=file)
    print(p+' x ',end='')
    print(p+' x ',end='',file=file)
    if ca%2!=0:
        print('~',end='')
        print('~',end='',file=file)
    print('P(x)')
    print('P(x)',file=file)
    s+=1

if ci%2==1:
    print('Step '+str(s)+': ~( ',end='')
    print('Step '+str(s)+': ~( ',end='',file=file)
    for i in range(1,5):
        print(supp[(ca)%2]+'('+str(i)+'))'+sign[q],end='')
        print(supp[(ca)%2]+'('+str(i)+'))'+sign[q],end='',file=file)
    print(supp[(ca)%2]+'(5)) )')
    print(supp[(ca)%2]+'(5)) )',file=file)
    s+=1

result=''
for i in range(1,5):
    result+=(supp[(ci+ca)%2]+'('+str(i)+'))'+sign[(ci+q)%2])
result+=(supp[(ci+ca)%2]+'(5))')

print('Step '+str(s)+': ',result)
print('Step '+str(s)+': ',result,file=file)
print('\nAnswer : ',result,'\n')
print('\nAnswer : ',result,'\n',file=file)

file.close()