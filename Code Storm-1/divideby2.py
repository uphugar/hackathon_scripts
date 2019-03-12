import sys
import decimal

def remove_zeroes(num):
    try:
        dec = decimal.Decimal(num)
    except:
        return 'bad'
    tup = dec.as_tuple()
    delta = len(tup.digits) + tup.exponent
    digits = ''.join(str(d) for d in tup.digits)
    if delta <= 0:
        zeros = abs(tup.exponent) - len(tup.digits)
        val = '0.' + ('0'*zeros) + digits
    else:
        val = digits[:delta] + ('0'*tup.exponent) + '.' + digits[delta:]
    val = val.rstrip('0')
    if val[-1] == '.':
        val = val[:-1]
    if tup.sign:
        return '-' + val
    return val

t=input()
count=0
test_list=[]
while(count<int(t)):   
    n=input()
    test_list.append(n)
    count+=1
result_list=[]
decimal.getcontext().prec=200
for item in test_list:    
    result=decimal.Decimal(1.0)/decimal.Decimal(2**item)
    val=str('{0:.202f}'.format(result))
    res=remove_zeroes(val)
    print res
