import sys
from collections import Counter,defaultdict
def find_max(inlist):
    profile=Counter(inlist).most_common()[0][0]
    maxval=Counter(inlist).most_common()[0][1]
    return profile

def BFS(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def create_dict(info_list):
    diction=defaultdict(list)
    for k,v in info_list:
        diction[k].append(v)
    #return diction.items()
    return diction

n=input()
i=0
info=[]
followed=[]
following=[]
while(i<int(n)):
    vals=raw_input()
    inp=vals.split(',')
    followed.append(int(inp[0]))
    following.append(int(inp[1]))
    info.append([int(inp[0]),int(inp[1])])
    i+=1
operation=raw_input()
inputs=operation.split(',')
maxfollowed=find_max(followed)
maxfollowing=find_max(following)
dictionary=create_dict(info)
retval=BFS(dictionary,int(inputs[0]),int(inputs[1]))
if retval is not None:
    short_path= len(retval)
else:
    short_path=0
print str(maxfollowed)+','+str(maxfollowing)+','+str(short_path)
