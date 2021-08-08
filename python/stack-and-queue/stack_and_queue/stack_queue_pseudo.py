from stack_and_queue.stack_and_queue  import Stack
class Pseudo_queue:
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


    # def __str__(self):
    #     string = ""
    #     current = self.push_stack.top
    #     current1 = self.pop_stack.top
    #     if current:
    #         return str(current.value)
    #     elif current1:
    #         return str(current1.value)
    #     else:
    #         return ("empty string")

test=Pseudo_queue()
test.enqueue(3)
test.enqueue(4)
test.enqueue(6)
test.enqueue(7)
# test.dequeue()
# test.dequeue()
# test.dequeue()

print(test.dequeue())
print(test.dequeue())
print(test.dequeue())
