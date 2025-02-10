import sys
input = sys.stdin.readline

n=int(input())
points = [[-1, "",False] for _ in range(2 * n)]
count=[0]*(n+1)
for i in range(n):
    line=input().split()
    l=int(line[0])
    r=int(line[1])
    points[i][0]=l
    points[i][1]="l"
    points[i+n][0]=r
    points[i+n][1]="r"
    if(l==r):
        points[i][2]=True
        points[i+n][2]=True
points.sort(key=lambda x: (x[0], x[1] == "l"))

x=0  
i=0
while(i <2*n-1):
    if(points[i][2]):
        i+=1
        continue
    j=i+1
    while(points[j][2]):
        if(j==2*n-1):
            break
        j+=1
    g=points[j][0]-points[i][0]-1
    if(not g>0):
        g=0
        
    if(points[i][1] == "l"):
        x += 1
        if points[j][1]=="r":
            count[x]+=g
            x -= 1
            
        elif points[j][1]=="l":
            count[x]+=g
            
    elif points[i][1] == "r":
        if points[j][1]=="r":
            count[x]+=g
            x-= 1
            
        elif points[j][1]=="l":
            count[x]+=g
            
    i=j


        
points.sort(key=lambda x: (x[0], x[1] == "r"))

i=0     
l=0      
while(i<2*n):
    
    if(points[i][1]=="l"):
        l+=1
        if(points[i][0]==points[i-1][0]):
            count[l-1]-=1
        count[l]+=1
    else:
        if(points[i][0]==points[i-1][0]):
            l-=1
            i+=1
            continue
        count[l]+=1
        l-=1    
    
    i+=1   
print(" ".join(map(str, count[1:])))