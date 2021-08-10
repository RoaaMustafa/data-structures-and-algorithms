from stack_and_queue.stack_and_queue import Queue

class AnimalShelter:
  def __init__(self) :
      self.cat=Queue()
      self.dog=Queue()

  def enqueue(self,animal):
      if animal=='cat' :
        self.cat.enqueue(animal)

      elif animal=='dog' :
        self.dog.enqueue(animal)

      else :
        return 'The animal is not in the list'


  def dequeue(self,animal):
    if animal =='cat' and self.cat.front:
      return self.cat.dequeue()


    if animal =='dog'  and self.dog.front:
       return self.dog.dequeue()

    if animal =='dog' or animal =='cat':
        return 'The animal not there'
    else :
      return 'The animal not in the shelf for ignore it'


catDog=AnimalShelter()
catDog.enqueue('cat')
catDog.enqueue('cat')
catDog.enqueue('dog')
catDog.enqueue('dog')

# print(catDog.dequeue('dodg'))
print(catDog.dequeue('dog'))
print(catDog.dequeue('dog'))
