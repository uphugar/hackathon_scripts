import sys
from collections import Counter,defaultdict
import itertools
n=input()
i=0
hero_details=defaultdict(str)
while(i<int(n)):
    vals=raw_input()
    inp=vals.split(',')
    hero_details[int(inp[0])]=inp[1]
    i+=1

m=input()
j=0
fights=[]
while(j<int(m)):
    vals=raw_input()
    inp=vals.split(',')
    member_id=[]
    for it in inp[4].split('|'):
        member_id.append(int(it))
    fights.append([inp[0],int(inp[1]),int(inp[2]),int(inp[3]),sorted(member_id)])
    j+=1

##calculate net wins, with hero_id first and then wins
Net_wins=[]
for item in fights:
    net_win=item[1]-item[2]
    combs=list(itertools.combinations(item[4],2))
    nos=item[3]
    for combi in combs:
        if any(its[0]==combi for its in Net_wins):
            pass
        else:            
            Net_wins.append([combi,0])

        for ct in range(len(Net_wins)):
            if Net_wins[ct][0]==combi:
                Net_wins[ct][1]+=net_win
        
Net_wins.sort(key=lambda x:x[1], reverse=True)
result=[]
high=max(Net_wins,key=lambda x:x[1])
for winner in Net_wins:
    if winner[1]==high[1]:
        result.append(winner[0])
for final in result:
    print str(hero_details[final[0]])+' & '+str(hero_details[final[1]])
