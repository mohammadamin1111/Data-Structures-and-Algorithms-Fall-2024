a=[]
def input_value():
 for i in range(9):
    row=[]
    line=str(input())
    for j in range(len(line)):
        if(line[j]==']' or line[j]=='[' or line[j]==',' or line[j]=='"' ):
            continue
        elif(line[j].isdigit() or line[j]=='.'):
            row.append(line[j])
    a.append(row)                
 return            
  
  
def check_squares(x,y):
    l=[]
    for i in range(y,y+3):
        for j in range(x,x+3):
            if(a[i][j]=='.'):
                continue
            for k in range(len(l)):
                if(l[k]==a[i][j]):
                    return False
            l.append(a[i][j])    
    return True            
                      
def solve():
    for i in range (9):
        x=[]   
        for j in range(9):
            if(a[i][j]=='.'):
              continue  
            for k in range(len(x)):
                if(x[k]==a[i][j]):
                    return False
            x.append(a[i][j])    
    for j in range (9):
        x=[]   
        for i in range(9):
            if(a[i][j]=='.'):
              continue 
            for k in range(len(x)):
                if(x[k]==a[i][j]):
                    return False
            x.append(a[i][j])
    s1=check_squares(0,0)
    s2=check_squares(3,0)
    s3=check_squares(6,0)
    s4=check_squares(0,3)
    s5=check_squares(3,3)
    s6=check_squares(6,3)
    s7=check_squares(0,6)
    s8=check_squares(3,6)
    s9=check_squares(6,6)             
    return (s1 and s2 and s3 and s4 and s5 and s6 and s7 and s8 and s9)                        
            
            
input_value()
is_salem=solve()
if(is_salem):
    print("true")    
else:
    print("false")