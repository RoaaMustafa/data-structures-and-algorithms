class Node():
    def __init__(self,value=""):
        self.next=None
        self.value=value

class Stack():
    def __init__(self):
        self.top=None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        if self.is_empty():
            raise Exception("empty stack")
        temp=self.top
        self.top=self.top.next
        temp.next=None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise Exception("empty stack")
        return self.top.value

    def is_empty(self):
     return not self.top

    def __len__(self):
        counter=0
        while self.top:
            counter +=1
            self.pop()
        return counter




class Queue:
    def __init__(self):
        self.front=None
        self.rear=None


    def enqueue(self,value):
        node=Node(value)
        if self.is_empty():
            self.front=node
            self.rear=node
        self.rear.next=node
        self.rear=node


    def dequeue(self):
        if self.is_empty():
            raise Exception("empty equeue")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.value

    def peek(self):
       if self.is_empty():
           raise Exception("empty equeue")
       return self.front.value


    def is_empty(self):
     return not self.front

    def __len__(self):
        counter=0
        while self.front:
            counter +=1
            self.dequeue()
        return counter

test=Queue()
# test.enqueue(3)
# test.push(2)
# test.push(1)
# test.e()
# test.dequeue()

print(test.__len__())
# test=Stack()
# test.push(1)
# test.push(2)


# print(test.peek())
