import sys
import os

sys.setrecursionlimit(150000)


def BlueRuby(b,r):
    #conditions for blue or red
    
    if (b>0):
        return "b"
    elif r>0:
        return "r"

def RedRuby(g,y):
    #conditions for green or yellow 
    if g>0:
        return "g"
    elif (y>0):
        return "y"

try:
    b = int(input())
    r = int(input())
    y = int(input())
    g = int(input())
except:
    b=0
    r=0
    y=0
    g=0
    
length=0
if(b>2000 or r>2000 or y>2000 or g>2000):
    if(b>2000):
        b=2000
    if (r>2000):
        r=2000
    if (y>2000):
        y=2000
    if(g>2000):
        g=2000
        
string=""
#inputs={"b":b,"r":r,"y":y,"g":g,"l":length}
Final=False
if(b>0 or r>0 or y>0 or g>0):
    while(Final!=False):
        if(b>0):
            str1=BlueRuby(b,r)
            if(str1="b"):
                b=b-1
                string=string+str1
            elif(str1="r"):
                r=r-1
                string=string+str1
        elif r>0:
            str1=RedRuby(g,y)
            if(str1="g"):
                g=g-1
                string=string+str1
            elif(str1="y"):
                y=y-1
                string=string+str1
        elif y>0:
            str1=BlueRuby(b,r)
        elif g>0:
            g=g-1
            inputs={"b":b,"r":r,"y":y,"g":g,"l":length+1}
            inputs=RedRuby(inputs)
        else:
            Final=True
            print(len(string))
        #print (len(string))
else:
    print (0)
