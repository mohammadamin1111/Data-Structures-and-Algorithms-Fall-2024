def max_size_prefix_postfix(pattern):
    f=[0]
    j=0
    n=len(pattern)
    for i in range(1,n):
        j = f[i-1]
        while (True):
            if(pattern[i]==pattern[j] or j==0):
                break
            j = f[j - 1]
        if(pattern[i]==pattern[j]):
            f.append(j+1)
        else:
            f.append(0)            
    return f[n-1]


n=int(input())
x=input().split(" ")
l=x[0]
for i in range(1,n):
    l_prim=l[-len(x[i]):]
    k=max_size_prefix_postfix(x[i]+"$"+l_prim)
    l=l+x[i][k:]
    
    
print(l)    
    