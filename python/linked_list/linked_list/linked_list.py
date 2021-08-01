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
  print(ll.includes(7))
