
input=input();
x=input[1:len(input)-1]
a="";
sign='n'
start=False
max=2**31-1
min=-2**31
for i in range(len(x)):
    if(x[i]==' ' and start):
        break
    if(x[i]==' '):
        continue
    elif((x[i]=='+' or x[i]=='-')):
        if(not sign=='n'):
            break
        if(start):
            break
        sign=x[i]
    elif(not x[i].isdigit()):
        break
    elif (x[i]>='0' and x[i]<='9'):
        start=True
        a=a+(x[i])
if(a==""):
    print(0)
else:            
  if(sign=='-'):
    a=sign+a  
  if(int(a)>max):
      a=str(max)
  elif(int(a)<min):
      a=str(min)              
  print(int(a)) 
  
   