 class Node:
  def __init__(self, value=""):
    self.value = value
    self.next = None

  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)

class LinkedList():
  def __init__(self):
    self.head = None

  def insert(self, value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node

  def append(self,value):
      current_node=Node(value)
      last_node=self.head
      while current_node:
          if last_node.next==current_node:
           break
      last_node=last_node.next

  def insert_after(self,old_value,new_value):
    new_node=Node(new_value)
    current=self.head
    temporary=self.head
    while current.next!=None:
      if current.new_value==old_value:
        temporary=temporary.next
        current.next=new_node
        current=current.next
        current.next=temporary
        return
      current=current.next
      temporary=temporary.next
    self.append(new_value)


  def insert_before(self,value,new_value):
    node=Node(new_value)
    current=self.head
    temporary=self.head
    if current.value==value:
      self.insert(new_value)
      return
    while(current.next.new_value!= value):
      current=current.next
    temporary = current.next
    current.next=node
    node.next = temporary

  def includes(self,vlaue):
     current=self.head
     while current :
         print(current.value)
         if vlaue ==current.value:
            return True
         current=current.next
     return False

  def __str__(self):
    string = ""
    current = self.head
    while current:
      string += f"{str(current.value)} -> "
      current = current.next
    string += "None"
    return string

  def __iter__(self):
    current = self.head
    while current:
      yield current.value
      current = current.next



  def __repr__(self):
    return "LinkedList()"
if __name__ == "__main__":
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(5)
  ll.insert(7)
  ll.append(3)
  print(ll.includes(7))
