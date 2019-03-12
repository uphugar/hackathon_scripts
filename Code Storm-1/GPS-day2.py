import sys
from math import radians,cos,sin,asin,sqrt,pi,atan2
import datetime
def haversine(lon1, lat1, elev1 ,lon2, lat2,elev2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon=abs(lon2-lon1)
    dlat=abs(lat2-lat1)
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    #c = 2 * asin(sqrt(a))
    dist=6378*2*asin(sqrt(a))
    elev_diff=abs(elev2-elev1)
    if elev_diff>0:
        hypo=sqrt(dist*dist+elev_diff*elev_diff*0.000001)
        dist=hypo
    return dist

n=input()
i=0
track_points=[]
while(i<int(n)):
    inp=raw_input()
    point_details=inp.split(',')
    point=[]
    for it in point_details:
        point.append(it)
    track_points.append(point)
    i+=1

p=0
distance=0.0
time_diff=0.0
while(p<n-1):
    point1=track_points[p]
    point2=track_points[p+1]
    elevation1=float(point1[0])
    time1=point1[1]
    lat1=float(point1[3])
    long1=float(point1[4])
    
    elevation2=float(point2[0])
    time2=point2[1]
    lat2=float(point2[3])
    long2=float(point2[4])
    p+=1
    distance+=haversine(long1,lat1,elevation1,long2,lat2,elevation2)
    time_diff+=(datetime.datetime.strptime(time2, '%Y-%m-%dT%H:%M:%SZ')-datetime.datetime.strptime(time1, '%Y-%m-%dT%H:%M:%SZ')).total_seconds()

print time_diff
avg_speed=(distance/time_diff)*3600
print str(distance)+','+str(avg_speed)
