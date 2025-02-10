a=eval(input())
n=len(a)
s=[a[0]]
for i in range(1,n):
    s.append(a[i])
    while(len(s)>1):
        if(not(s[-1]<0 and s[-2]>0)):
            break
        if(s[-1]+s[-2]==0):
                s.pop()
                s.pop()
        elif(s[-1]+s[-2]<0):      
                temp=s[-1]
                s.pop()
                s.pop()
                s.append(temp)
        elif(s[-1]+s[-2]>0):      
                s.pop()
                         
   
print("[" + ",".join(map(str, s)) + "]")
         
            
                        
         