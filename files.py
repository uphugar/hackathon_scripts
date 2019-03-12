import os
import pdb
import csv
rootdir='E:\\'
string='.mp4'
resultlist=[['File name','size in kb','full path','link']]
for root,subdirs,files in os.walk(rootdir):
##    print root
##    print subdirs
##    print files
    #pdb.set_trace()
    for file1 in files:
        if file1.lower().endswith(string):
            #pdb.set_trace()
            #temp=os.stat(root+'\\'+file1)
            path=root+'\\'+file1
            temp2=os.path.getsize(path)
            link=path.replace('\\','/')
            link='file:///'+link
            temp=temp2/1024
            resultlist.append([file1,temp,path,link])
            
print resultlist
w=open('Videofiles.csv','wb')
a=csv.writer(w)
a.writerows(resultlist)
