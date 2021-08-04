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
    self.data=None

  def insert(self, value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node

  def append(self,value):
      node=Node(value)
      current=self.head
      if current==None:
          self.insert(value)
          return
      while current.next!=None:
          current=current.next
      current.next=node

  def insert_after(self,old_value,value):
    node=Node(value)
    current=self.head
    temp=self.head
    while current.next!=None:
      if current.value==old_value:
        temp=temp.next
        current.next=node
        current=current.next
        current.next=temp
        return
      current=current.next
      temp=temp.next
    self.append(value)


  def insert_before(self,old_value,value):
    node=Node(value)
    current=self.head
    temp=self.head
    if current.value==old_value:
      self.insert(value)
      return
    while(current.next.value!= old_value):
      current=current.next
    temp = current.next
    current.next=node
    node.next = temp

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

  def __len__(self):
    counter = 0
    current = self.head
    while current:
      counter += 1
      current = current.next
    return counter

  def kthFromEnd(self,num):
      num1=len(self)-1
      if num1<num:
          return ("out of the range")
      num_of_loop=(len(self)-num)-1
      current=self.head
      while num_of_loop >0 :
          current=current.next
          num_of_loop -=1
      return current.value
  def __repr__(self):
    return "LinkedList()"

  def reverse(self):
      pass
      prev=None
      current =self.head
      while(current is not None):
          next=current.next
          current.next=prev
          prev=current
          current=next
      self.head=prev


def zipLists(llist1, llist2):
    current1 = llist1.head
    current2 = llist2.head

    if current1 == None or current2 == None:
        if current1:
            return llist1.__str__()
        elif current2:
            return llist2.__str__()
        else:
         return "Linked lists are both Empty "

    zip_list = []
    while current1 or current2:
        if(current1):
            zip_list+=[current1.value]
            current1 = current1.next
        if(current2):
            zip_list+=[current2.value]
            current2 = current2.next
    insertion_values=''
    for item in zip_list:
      insertion_values+=f'{item}-> '
    insertion_values+='None'
    return insertion_values



if __name__ == "__main__":
  ll = LinkedList()
  ll.insert(1)
  ll.insert(2)
  ll.insert(5)
  print(ll)
  ll.reverse()
  print(ll)

#   ll.insert(7)
#   ll.append(3)
  # ll.insert_after(7,8)
  # ll.insert_before(7,6)
#   llist1 = LinkedList()
#   llist1.append(1)
#   llist1.append(3)
#   llist1.append(5)
#   llist2 = LinkedList()
#   llist2.append(2)
#   llist2.append(4)
#   llist2.append(6)
#   print(llist1.__str__())
#   print(llist2.__str__())
#   print(zipLists(llist1,llist2).__str__())
