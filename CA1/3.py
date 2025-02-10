a=eval(input());
path=[]
k=0
i=0
j=0
state=0
rows=len(a)
cols=len(a[0])
r=rows
c=cols
while (True):
    path.append(a[i][j])
    k+=1
    if(k==rows*cols):
      break
    if(j==len(a[0])-1 and state==0):
        del a[0]
        state+=1
        i=0
        continue
    elif(state==1 and i==len(a)-1 ) :
        index=len(a[0])-1
        for row in a:
            del row[index]   
        state+=1
        j = len(a[0]) - 1
        continue
    elif(j==0 and state==2):
        del a[len(a)-1]
        state+=1
        i = len(a) - 1
        continue
    elif(state==3 and i==0 ) :
        for row in a:
            del row[0]
        state=0;
        j=0
        continue       
        
    if(state==0):
      j+=1
    elif(state==1):
      i+=1
    elif(state==2):
      j-=1
    elif(state==3):
      i-=1              
    
print(path)    
            
        
                