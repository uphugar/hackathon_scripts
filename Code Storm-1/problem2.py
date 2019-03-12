import sys
tests=input('enter no of tests')
i=0
question_list=[]
while(i<int(tests)):
    temp=input('enter questions')
    question_list.append(temp)
    i+=1

for no_of_que in question_list:
    if no_of_que<113:   
        if no_of_que%2==0:
            mod_res10=no_of_que%10
            mod_res12=no_of_que%12
            if mod_res12==0:
                no_of_pages=no_of_que/12
                print str(no_of_pages)
                #break
            else:
                something=0
                
        else:
            print '-1'
    else:
        print '-1'
