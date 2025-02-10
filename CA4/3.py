import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

inputt=input().split()
n=int(inputt[0])
m=int(inputt[1])

visited=[False]*(n+1)
p_string=input().split()
p=[int(x) for x in p_string]

g=[[] for _ in range(n+1)]

for i in range(1,n+1):
    g[i].append(p[i-1])

for i in range(m):
    
    inputt=input().split()
    a=int(inputt[0])
    b=int(inputt[1])
    g[a].append(b)
    g[b].append(a)
x=[]
y=[]

def dfs(node):

    if(visited[node]):
        return
    visited[node]=True
    x.append(node)
    y.append(g[node][0])
    for i in range(1,len(g[node])):
        dfs(g[node][i]) 
    return    

answer=0  
for j in range(1,n+1):
    if(not visited[j]):
       
        dfs(j)
        set1=set(x)
        set2=set(y)
        answer+=len(set1&set2)
        x.clear()
        y.clear()


print(answer)        