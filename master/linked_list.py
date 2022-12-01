
class LinkedList(object):
    is_empty=True
    size = 0
    
    class Node(object):
    
        def __init__(self, value, next=None, previous=None):
            self.value = value
            self.next = next
            self.previous = previous
            self.id = id(self)
            
        def __repr__(self) -> str:
            return f"{self.value}:{self.id}:{id(self.next)}:{id(self.previous)}:{id(None)}"
            
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
        self.size = self._size()    
        
    def add_last(self, item):
        node = self.Node(item)
        if  self.is_empty:
            self.first = node
            self.last = node
            self.is_empty = False
            self.size+=1

        else:
            old_last = self.last
            self.last.next = node
            self.last = node
            self.last.previous = old_last
            self.size+=1

     
    
    
    def add_first(self, item):
        node = self.Node(item)
        if self.is_empty:
            self.first = node
            self.last = node
            self.is_empty = False
            self.first.previous = None
            self.size +=1
        else:
            first_node_address = self.first
            
            self.first = node
            self.first.next = first_node_address
            first_node_address.previous = self.first
            self.size+=1


    def __repr__(self) -> str:
        return f"[{self.first.value}:{self.first.next}] ......  [{self.last. value}:{self.last.next}]"
        
        
        
        
    def delete_first(self):
        if self.is_empty:
            raise BaseException("The linked list is empty!")
        old_first = self.first
        self.first = old_first.next
        self.first.previous = None
        self.size-=1
        del old_first
    
    def delete_last(self):
        if self.is_empty:
            raise BaseException("The linked list is empty!")
        current = self.first
        if current.next == None:
            self.is_empty = True
            self.first = None
            self.last = None
            current = None
            self.size-=1
        while current != self.last:
            if current.next != self.last:
                current = current.next
            else:
                self.last = current
                self.last.next = None
                self.size-=1

                
    
    def _size(self):
        length = 0
        if self.is_empty:
            return 0
        else:
            current = self.first
        while current != self.last:
            current = current.next
            length +=1
        return length + 1
    
    
    
    def contains(self, value):
        current = self.first
        while current != None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False
        
    
    
    
    def indexof(self, item):
        index = 0
        current = self.first
        while current != None:
            if(current.value == item):
                return index
            else:
                current = current.next
                index = index + 1
        return -1
    
    def reverse(self):
        old_last = self.last
        current = self.last
        while current != self.first:
            current.next = current.previous
            current = current.next
        self.last = self.first
        self.last.previous = self.first.next
        self.first = old_last
        self.first.previous = None
        self.last.next = None
        
        current = self.first
        while current != self.last:
                current.next.previous = current
                current = current.next
                
    
    def convert_to_list(self):
        if not self.is_empty: 
            current = self.first
            output = list()
            while current.next != None:
                output.append(current)
                current = current.next
            output.append(self.last)
            return output
        else:
            raise BaseException("Linked List is empty!!")    
    
    def print_middle(self):
        if self.is_empty:
            raise BaseException("List is empty!")
        else:

            current_index = 1
            first_node = self.first
            second_node = self.first
            while second_node != self.last:
                first_node = first_node.next
                if second_node.next.next:
                    second_node = second_node.next.next
                    current_index +=1
                else:
                    return current_index, current_index+1
            return current_index
        
        
    
    def find_kth_node(self, k):
        if k == 1 or k == 0 or k<0:
            return self.last
        elif k > self._size():
            raise BaseException("K is greatar than the size of the linked list!")
        else:
            flag = 1
            first_node = self.first
            while first_node != self.last:
                if flag:
                    first_node = first_node.next
                    flag+=1
                    if flag == k:
                        second_node = self.first
                        flag = False 
                else:
                    first_node = first_node.next
                    second_node = second_node.next
            first_node = self.last
            return second_node
        
linked_list = LinkedList()


# for item in linked_list.convert_to_list():
#     print(item, end='\n')
print("-------------------------------------------")
print(linked_list.print_middle())
# linked_list.reverse()

# for item in linked_list.convert_to_list():
#     print(item, end='\n')
    
# linked_list.reverse()
# print("-------------------------------------------")

# for item in linked_list.convert_to_list():
#     print(item, end='\n') 
pass
