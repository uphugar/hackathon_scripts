import sys
import os

sys.setrecursionlimit(255000)

def BlueRuby(inputs):
    #conditions for blue or red
    b=inputs["b"]
    r=inputs["r"]
    length=inputs["l"]
    #print (b,r,length)
    #ruby=inputs["ruby"]
    if (b>0):
        inputs["b"]=b-1
        inputs["l"]=length+1
        #inputs["ruby"]=ruby+"b"
        inputs=BlueRuby(inputs)
    elif r>0:
        inputs["r"]=r-1
        inputs["l"]=length+1
        #inputs["ruby"]=ruby+"r"
        inputs=RedRuby(inputs)
    return inputs

def RedRuby(inputs):
    #conditions for green or yellow 
    g=inputs["g"]
    y=inputs["y"]
    length=inputs["l"]
    #ruby=inputs["ruby"]
    if g>0:
        inputs["g"]=g-1
        inputs["l"]=length+1
        inputs=RedRuby(inputs)
    elif (y>0):
        inputs["y"]=y-1
        inputs["l"]=length+1
        inputs=BlueRuby(inputs)
    return inputs

b = int(input())
r = int(input())
y = int(input())
g = int(input())

length=0
inputs={"b":b,"r":r,"y":y,"g":g,"l":length}
if(b>0 or r>0 or y>0 or g>0):
    if(b>0):
        b=b-1
        inputs["b"]=b
        inputs["l"]=length+1
        inputs=BlueRuby(inputs)
        r=inputs["r"]
        b=inputs["b"]
        y=inputs["y"]
        g=inputs["g"]
        length=inputs["l"]
    elif r>0:
        r=r-1
        inputs={"b":b,"r":r,"y":y,"g":g,"l":length+1}
        inputs=RedRuby(inputs)
        r=inputs["r"]
        b=inputs["b"]
        y=inputs["y"]
        g=inputs["g"]
        length=inputs["l"]
    elif g>0:
        g=g-1
        inputs={"b":b,"r":r,"y":y,"g":g,"l":length+1}
        inputs=RedRuby(inputs)
        r=inputs["r"]
        b=inputs["b"]
        y=inputs["y"]
        g=inputs["g"]
        length=inputs["l"]
    elif y>0:
        y=y-1
        inputs={"b":b,"r":r,"y":y,"g":g,"l":length+1}
        inputs=BlueRuby(inputs)
        r=inputs["r"]
        b=inputs["b"]
        y=inputs["y"]
        g=inputs["g"]
        length=inputs["l"]
    print (inputs["l"])
else:
    print (0)
