import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        pass

    def __init__(self):
        self.h=[]
       

    def bubble_up(self, index):
        if( not isinstance(index, int)):
            raise Exception (INVALID_INDEX)
        if(index not in range(len(self.h))):
            raise Exception(OUT_OF_RANGE_INDEX)
        while(True):
            if(not index>0):
                break
            if self.h[index] < self.h[(index - 1)//2]:
                self.h[index], self.h[(index - 1)//2]= self.h[(index - 1) // 2],self.h[index]
                index = (index -1) // 2
            else:
                break
                    
    def bubble_down(self, index):
        if( not isinstance(index, int)):
            raise Exception (INVALID_INDEX)
        if(index not in range(len(self.h))):
            raise Exception(OUT_OF_RANGE_INDEX)
        while(True):
             if(2*index+2 >= len(self.h)):
                 break
             if(self.h[index] >= self.h[2*index+1] and  self.h[2*index+1] <=self.h[2*index+2]):
                   temp= self.h[index]
                   self.h[index]=self.h[2*index+1]
                   self.h[2*index+1]=temp
                   index=2*index+1
             elif(self.h[index] >= self.h[2*index+2] and self.h[2*index+2] <=self.h[2*index+1]):
                   temp= self.h[index]
                   self.h[index]=self.h[2*index+2]
                   self.h[2*index+2]=temp
                   index=2*index+2
             else:
                 break
     
    def heap_push(self, value):
        self.h.append(value)
        self.bubble_up(len(self.h)-1)

    def heap_pop(self):
   
        if(len(self.h)==0):
            raise Exception(EMPTY)
        root=self.h[0]
        self.h[0]=self.h[len(self.h)-1]
        self.h.pop()
        if(not len(self.h)==0):
          self.bubble_down(0)
        return root

    def find_min_child(self, index):
        if( not isinstance(index, int)):
            raise Exception (INVALID_INDEX)
  
        if(index not in range(len(self.h))):
            raise Exception(OUT_OF_RANGE_INDEX)
        if(self.h[2*index+1]<=self.h[2*index+2]):
            return 2*index+1
        else:
            return 2*index+2    

    def heapify(self, *args):
        self.h=list(args)
        for i in range(len(self.h)//2-1,-1,-1):
    
            self.bubble_down(i)
       


class HuffmanTree:
    class Node:
        def __init__(self,l,re):
            self.re = re
            self.left = None 
            self.right = None 
            self.letter=l
            self.bit_code=None
            

    def __init__(self):
        self.root=None
        self.letters=[]
        self.repaet=[]
        self.length_code=[]

    def set_letters(self, *args):
        self.letters=list(args)

    def set_repetitions(self, *args):
        self.repaet=list(args)

    def set_text(self, text):
        d={} 
        for c in text:
            if(c in d):
                d[c]+=1
            else:
                d[c]=1
        
        self.d = dict(sorted(d.items(), key=lambda item: item[1]))          
        self.repaet=list(d.values())
        self.letters=list(d.keys())   

    def build_tree(self):
        s=[]
        for i in range(len(self.letters)):
            node=self.Node(self.letters[i],self.repaet[i])
            s.append(node)
        while(True):
                if(len(s)==1):
                    self.root=s[0]
                    break
                l=min(s, key=lambda x : x.re)
                s.remove(l)
                r=min(s, key=lambda x : x.re)
                s.remove(r)
                new_node=self.Node(None,l.re+r.re)
                new_node.left=l
                new_node.right=r
                s.append(new_node)
            
        

    def get_compressed_length(self):
          
          def bfs(current):
                x=0
                q=[]
                q.append((current,0))
                while(not len(q)==0):
                    current=q[0]
                    if(not current[0].letter==None):
                        x+=current[1]*current[0].re
                    q.pop(0)
                    if( not current[0].left==None):
                        q.append((current[0].left , current[1]+1))
                    if( not current[0].right==None):    
                        q.append((current[0].right , current[1]+1))
                return x
          print(bfs(self.root)) 


class Bst:
    class Node:
        def __init__(self, key):
            self.key = key 
            self.left = None 
            self.right = None 
             

    def __init__(self):
        self.root=self.Node(None)

    def insert(self, key):
        if(self.root.key==None):
           self.root.key=key
        else:
            current_node=self.root
            while(True):
                if(key<current_node.key):
                    if(current_node.left==None):
                        current_node.left=self.Node(key)
                        break
                    else:
                        current_node=current_node.left
                            
                else:
                    if(current_node.right==None):
                        current_node.right=self.Node(key)
                        break
                    else:
                        current_node=current_node.right
                        
                
    def preorder(self):
        
        def pre_order(current):
            if(current==None):
                return
            print(current.key,end=" ")
            pre_order(current.left)
            pre_order(current.right)
            
        
        
        pre_order(self.root)
        print("")    

    def inorder(self):
        def in_order(current):
            if(current==None):
                return
            
            in_order(current.left)
            print(current.key,end=" ")
            in_order(current.right)
            
        
        
        in_order(self.root)
        print("")   

    def postorder(self):
        def post_order(current):
            if(current==None):
                return
            
            post_order(current.left)
            post_order(current.right)
            print(current.key,end=" ")
            
        
        
        post_order(self.root)
        print("")   

class Runner:
    ds_map = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()

        args = [x.strip() for x in args_list.split(',')] if args_list != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[item_name], func_name)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
