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


class pseudo_queue:
    def __init__(self):

        self.push_stack=Stack()
        self.pop_stack=Stack()

    def enqueue(self,value):
        self.push_stack.push(value)


    def dequeue(self):
         if self.pop_stack.is_empty():
            while self.push_stack.top != None:
                self.pop_stack.push(self.push_stack.pop())
         return (self.pop_stack.pop())

    def __str__(self):
        string = ""
        current = self.push_stack.top
        current1 = self.pop_stack.top
        if current:
            return str(current.value)
        elif current1:
            return str(current1.value)
        else:
            return ("empty string")

test=pseudo_queue()
test.enqueue(3)
test.enqueue(4)
test.enqueue(6)
test.enqueue(7)
# test.dequeue()
# test.dequeue()
# test.dequeue()

print(test)

# test=Queue()
# test.enqueue(3)
# test.push(2)
# test.push(1)
# test.e()
# test.dequeue()

# print(test.__len__())
# test=Stack()
# test.push(1)
# test.push(2)


# print(test.peek())
