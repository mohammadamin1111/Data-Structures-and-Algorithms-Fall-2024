import sys
import re


class Queue:
    def __init__(self):
        self.q=[]
    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        if(self.empty()):
            pass
        else:
            return self.q.pop(0)

    def size(self):
        return(len(self.q))
    def empty(self):
        return(len(self.q)==0)

    def one_line_str(self):
        self.q=[int(n) for n in self.q]
        return str(self.q).replace(",","")[1:-1]


class Stack:
    def __init__(self, capacity=10):
        self.s=[]
        self.c=capacity
    def push(self, value):
        if (self.size()<self.c):
           self.s.append(value)

    def pop(self):
        if(self.empty()):
            pass
        else:
            return self.s.pop()

    def put(self, value):
        if(not self.empty()):
            self.pop()
            self.push(value)

    def peek(self):
        if(self.empty()):
            pass
        else:
            return self.s[-1]

    def expand(self):
        self.c*=2

    def capacity(self):
        return self.c

    def size(self):
        return(len(self.s))

    def empty(self):
        return(len(self.s)==0)

    def one_line_str(self):
       if(not self.empty()): 
            self.s=[int(n) for n in self.s]
            return str(self.s).replace(",","")[1:-1]


class Node:
    def __init__(self, value):
        self.node=value


class LinkedList:
    def __init__(self):
        self.ll=[]

    def insert_front(self, value):
        self.ll.insert(0, value)

    def insert_back(self, value):
        
        self.ll.append(value)

    def reverse(self):
        self.ll.reverse()

    def one_line_str(self):
        self.ll=[int(n) for n in self.ll]
        return str(self.ll).replace(",","")[1:-1]


class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
