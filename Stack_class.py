from pythonds.basic.stack import Stack

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
    def pop(self):
        return self.items.pop()
    def print_stack(self):
        for i in self.items:
            print(i)
    
