result = []
def gcd_1(m,n):
    z=abs(m-n)
    if (m-n)==0:
        return n
    else:
        return gcd_1(z,min(m,n))
                       
n = input()
v=0
while v < int(n):
    ab = raw_input()
    ablist = ab.split()
    a = int(ablist[0])
    b = int(ablist[1])
    arrA = []
    arrB = []
    arrA = range(1,a+1)
    arrB = range(1,b+1)
    #pdb.set_trace()
    v = v+1
    list_1 =[]
    list_1 = [(y, x) for y in arrB for x in arrA]
    list_2 = []
    count = 0
    for item in list_1:
        list_2 = str(item).replace('(','').replace(')','').split(',')
        res = gcd_1(int(list_2[0]), int(list_2[1]))
        if res == 1:
            count = count+1
    result.append(count)


for item in result:
    print item




