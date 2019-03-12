import datetime
import pdb

people=['Uday','Srinivas','Adarsh','Sarvesh','Venkanna']
print people[0]
str1=[]
today=datetime.datetime.today()
j=0
week=0
strbfr='Date, Person\n'
for i in range(30):
    #pdb.set_trace()
    today+=datetime.timedelta(days=1)
    week=i/7
    if today.isoweekday()<6:
        #temp=str(today)+','+people[i%5]
        str1.append(str(today.day)+'/'+str(today.month)+'/'+str(today.year)+':'+people[(j+week)%5])
        strbfr=strbfr+str(today.day)+'/'+str(today.month)+'/'+str(today.year)+','+people[(j+week)%5]+'\n'
        j=j+1
    else:
        str1.append(str(today.day)+'/'+str(today.month)+'/'+str(today.year)+', its a weekend enjoy!!')
        strbfr=strbfr+str(today.day)+'/'+str(today.month)+'/'+str(today.year)+', its a weekend enjoy!!\n'
        
print str1
with open('file.csv','wb') as f1:
    f1.write(strbfr)
    f1.close()
