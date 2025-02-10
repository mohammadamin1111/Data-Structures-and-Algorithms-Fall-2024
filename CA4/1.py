inputt=input().split()
n=int(inputt[0])
m=int(inputt[1])
q=[]
visited = set()
q.append((n,0))
while(q):
    x,y=q.pop(0)
    if(x==m):
        print(y)
        exit()
    s=[x-1,2*x]    
    if(x>m):
      s.pop()
    for u in s:
      if(not u in visited):          
        q.append((u,y+1))
        visited.add(u)