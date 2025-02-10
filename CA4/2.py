import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

inputt=input().split()
n=int(inputt[0])
m=int(inputt[1])

eydi=[0]*(n+1)
visited=[False]*(n+1)


g = [[0] for _ in range(n + 1)]
for i in range(n-1):
    inputt=input().split()
    u=int(inputt[0])
    v=int(inputt[1])
    g[u].append(v)
    g[v].append(u)
    
for j in range(m):
    
    inputt=input().split()
    a=int(inputt[0])
    b=int(inputt[1])
    g[a][0]+=b
score=0    
def dfs(node):

    if(visited[node]):
        return
    visited[node]=True
    global score
    score+=g[node][0]
    eydi[node]=score
    for i in range(1,len(g[node])):
        dfs(g[node][i])
        
    score-=g[node][0]   
    return    
    
          
dfs(1)  
for i in range(1,len(eydi)):
    print(eydi[i],end=" ")