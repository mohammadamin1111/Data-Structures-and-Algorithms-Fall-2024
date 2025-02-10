a = eval(input())
a_rev=list(reversed(a))
k = int(input())
answer = []
n=len((a))
s1= []
s2=[]

for i in range (n):
    if(i%k==0):
        s1.append(a[i])
        maximum1=a[i]
    else:
        maximum1=max(maximum1,a[i])      
        s1.append(maximum1)
x=n%k        
for i in range (n):
    if(i%k==x or i==0):
        s2.append(a_rev[i])
        maximum2=a_rev[i]
    else:
        maximum2=max(maximum2,a_rev[i])      
        s2.append(maximum2)      

s2=list(reversed(s2))
j=0
while(True):
    answer.append(max(s2[j],s1[j-1+k]))
    if(j+k-1==n-1):
        break
    else:
        j+=1
print("[" + ",".join(map(str, answer)) + "]")
