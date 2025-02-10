states=['None','not None']
list=None
state=states[0]
while(True):
    x=input().split(' ')
    if(x[0]=='1'):
        state=states[1]
        list=[]
    elif(x[0]=='2'):
        list=None
        state=states[0]
    
    elif(x[0]=='3'):
        if(state=='None'):
            print("nulle")
        else:
                
            m=x[1]
            list.append(m)
    
    elif(x[0]=='4'):
        if(state=='None'):
            print("nulle")
        else:
            n=x[1]
            if(int(n)>=len(list)):
                print("oute")
            else:
                print(list[int(n)])    
            
                
    elif(x[0]=='5'):
        m=x[1]
        n=x[2]
        if(n=='0'):
            print("sefre")
        else:
            print(int(m)//int(n))    
    elif(x[0]=='6'):
        break
                            
        
   