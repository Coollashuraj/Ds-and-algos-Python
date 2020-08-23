# Create Node class
class Node:
 def __init__(self, value, next_node= None):
     self.value = value
     self.next_node = next_node

 def get_value(self):
     return self.value
 def get_next_node(self):
     return self.next_node

 def set_next_node(self,next_node):
     self.next_node = next_node

class LinkedList():

 def __init__(self, value = None):
     self.head_node = Node(value)

 def get_head_node(self):
     return self.head_node

 def append_list(self,new_value):
      new_node= Node(new_value)
      new_node.set_next_node(self.head_node)
      self.head_node = new_node

 def stringfy_list(self):
  str_list = ''
  current_node=self.get_head_node()
  while current_node:
      if current_node.get_value() != None:
          str_list += str(current_node.get_value()) + "\n"
          current_node= current_node.get_next_node()
  return str_list
  # Test case
ll = LinkedList(5)
ll.append_list(44)
ll.append_list(6)
ll.append_list(1)
print(ll.stringfy_list())
