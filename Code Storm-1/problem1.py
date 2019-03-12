import sys
N=input()
testvalue=raw_input()
testlist=testvalue.split()
i=0
for item in testlist:
        k=1
        while k<=int(item):
            if k%15==0:
                print 'FizzBuzz'
            elif k%3==0:
                print 'Fizz'
            elif k%5==0:
                print 'Buzz'
            else:
                print k
            k+=1
            if k==item:
                passed=False
