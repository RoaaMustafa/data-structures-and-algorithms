class Node:
  ''''
  THis the class is responsiple to create the Nodes
  '''
  def __init__(self, value=""):
    self.value = value
    self.next = None

  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)


class LinkedList():

  '''
  This Class Responsable For Creating LinkdeList
  '''
  def __init__(self):
    self.head = None

  def insert(self, value):
    node = Node(value)
    # print(node)
    if self.head:
      node.next = self.head

    self.head = node

  def includes(self,vlaue):
     current=self.head
     while current :
        #  print(current.value)
         if vlaue ==current.value[0]:
            return True
         current=current.next
     return False

  def append(self,value):
    new_node=Node(value)

    if self.head == None:
      self.head = new_node
    else:
      current=self.head
      while current.next:
        current=current.next
      current.next=new_node



ll = LinkedList()

ll.append(3)
ll.append(4)
print(ll.head.value)
print(ll.head.next.value)
