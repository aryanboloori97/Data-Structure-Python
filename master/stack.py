from enum import Enum

class Stack(object):
    container = list()
    
    def __init__(self, *args):
        self.container = list(args)
    
    def push(self, item):
        self.container.append(item)
        
    
    def pop(self):
        if not self.isEmpty():
            return self.container.pop()
        raise Exception("Empty stack!")
    
    def peek(self):
        if not self.isEmpty():
            return self.container[len(self.container) - 1]
        raise Exception("Empty stack!")
    
    def isEmpty(self):
        try:
            self.push(self.container.pop())
        except IndexError:
            return True
        return False
        

    def __repr__(self):
        return f"{self.container}"
stack = Stack(1, 2, 3, 4, 5)



def reverse_string(string:str):
    list_of_chars = list(string)
    reversed_text_list = []
    for _ in range(len(list(string))):
        reversed_text_list.append(list_of_chars.pop())
        
    reversed_text = "".join(reversed_text_list)
    return reversed_text
    








