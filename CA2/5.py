input_=input().split(" ")
x=int(input_[-1])
a=eval(input_[0][:-1])
n=len(a)
answer=[]
i=x-1
k=0
for _ in range(n):
    if (not i in range(n)):
            break
    
    answer.append(a[i])   
    k+=1
    if(k==x):
        k=0
        i+=(2*x-1)
    else:
        i-=1    

r=n%x
if(not r==0):
    answer.extend(a[-r:])
print("[" + ",".join(map(str, answer)) + "]")       