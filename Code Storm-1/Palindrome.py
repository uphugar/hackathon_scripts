import sys
import string
import pdb

def get_count(dictionary):
    maxval=0
    for char,value in dictionary.iteritems():
        if value%2==0:
            maxval=maxval+value
        elif value%2==1:
            maxval=maxval+value-1    
    return maxval

#pdb.set_trace()
N=input()
i=1
strings=[]
while(i<=int(N)):
    S=raw_input()
    strings.append(S)
    i=i+1

alphabets=string.lowercase
dictionary={}
for S in strings:
    for char in alphabets:
        number=S.count(char)
        dictionary[char]=number
    length=get_count(dictionary)
    if len(S)>length:
        print length+1
    else:
        print length
