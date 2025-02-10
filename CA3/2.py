import sys
input = sys.stdin.readline

class MinHeap:
    class Node:
        pass

    def __init__(self):
        self.h=[]
       

    def bubble_up(self, index):

        while(True):
            if(not index>0):
                break
            if self.h[index] < self.h[(index - 1)//2]:
                self.h[index], self.h[(index - 1)//2]= self.h[(index - 1) // 2],self.h[index]
                index = (index -1) // 2
            else:
                break
                    
    def bubble_down(self, index):
      
        
        while True:
            left_child =2*index+1
            right_child =2*index+2
            if(left_child>=len(self.h)):
                break

            smaller_child = left_child
            if(right_child<len(self.h) and self.h[right_child] < self.h[left_child]):
                smaller_child = right_child
            if(self.h[index]>self.h[smaller_child]):
                self.h[index],self.h[smaller_child]=self.h[smaller_child], self.h[index]
                index = smaller_child
            else:
                break

     
    def heap_push(self, value):
        self.h.append(value)
        self.bubble_up(len(self.h)-1)

    def heap_pop(self):
        if len(self.h) == 0:
           exit()  

        root=self.h[0]
        self.h[0]=self.h[len(self.h)-1]
        self.h.pop()
        if(not len(self.h)==0):
          self.bubble_down(0)
        return root

    def find_min_child(self, index):
        if(self.h[2*index+1]<=self.h[2*index+2]):
            return 2*index+1
        else:
            return 2*index+2    

    def heapify(self, *args):
        self.h=list(args)
        for i in range(len(self.h)//2-1,-1,-1):
            self.bubble_down(i)
    def size(self):
        return len(self.h)
    def print(self):
        print(self.h)
        
    def min(self):
        return self.h[0]            
t=int(input())  
while(t):     
    min_heap=MinHeap()
    max_heap=MinHeap()
    B=True
    while(True):
        
        # min_heap.print()
        # max_heap.print()
        x=int(input())
        if(B):
            median=x
            B=False
        if(x==-1):
            s=min_heap.size()+max_heap.size()
            # print(s)
            if(s%2==0):
                median=max_heap.heap_pop()
                
            else:
                if(min_heap.size()> max_heap.size()):
               
                  median=min_heap.heap_pop()
                else:
                    median=max_heap.heap_pop()  
                   
            print(abs(median))
            if(min_heap.size()-max_heap.size()>1):
                   temp=min_heap.heap_pop()
                   max_heap.heap_push(-temp)
            if(max_heap.size()-min_heap.size()>1):
                   temp=max_heap.heap_pop()
                   min_heap.heap_push(-temp) 
            s=min_heap.size()+max_heap.size()
            if(s%2==0):
                if(s==0):
                    B=True
                    continue
                else: 
                    median=-max_heap.min()
            
            else:
                if(min_heap.size()<=max_heap.size()):
                  median=-max_heap.min()
             
                else:
                     median=min_heap.min()       
        elif(x==0):
            break
            
        else:
            if(x>median):
               min_heap.heap_push(x)
               if(min_heap.size()-max_heap.size()>1):
                   temp=min_heap.heap_pop()
                   max_heap.heap_push(-temp)
                   
            else:
               max_heap.heap_push(-x)   
               if(max_heap.size()-min_heap.size()>1):
                   temp=max_heap.heap_pop()
                   min_heap.heap_push(-temp)
                   
            s=min_heap.size()+max_heap.size()
            if(s%2==0):
                median=-max_heap.min()
            
            else:
                if(min_heap.size()<=max_heap.size()):
                  median=-max_heap.min()
             
                else:
                     median=min_heap.min()   

                
    t-=1        