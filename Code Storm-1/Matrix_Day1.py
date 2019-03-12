import sys
n=input()
i=0
inMat=[]
while(i<int(n)):
    row_list=[]
    row=input()
    row_val=[]
    for it in row:
        row_val.append(it)
    inMat.append(row_val)
    i+=1
operation=raw_input()

def transpose(mat):
  res_transpose = zip(*mat)   
  return res_transpose

def counter_clockwise(mat):
  res_ccw = zip(*mat)[::-1]   
  return res_ccw

def clockwise(mat):
  res_cw = zip(*mat[::-1])
  return res_cw

def backward(mat):
  mat1 = zip(*mat)
  mat2 = zip(*mat1)[::-1]
  mat3 = zip(*mat2)[::-1]
  return mat3

def forward(mat):
  res_bw = zip(*mat)
  return res_bw


int_res = []
first_run = False
for item in operation:
    if first_run == False:
        int_res = inMat
        first_run = True
    if item == 'T':
        int_res = transpose(int_res)
    if item == 'A':
        int_res = counter_clockwise(int_res)
    if item == 'C':
        int_res = clockwise(int_res)
    if item == '/':
        int_res = backward(int_res)
    if item == '\\':
        int_res = forward(int_res)

for item in int_res:
    item1 = str(item) 
    left = item1.replace('(','')
    res = left.replace(')','')
    print res.replace(' ' ,'')
    
