from hashtable.linked_list import *

class HashTable :

  def __init__(self, size = 1024):

    self.size = size
    self._buckets = [None] *self.size



  def hash(self,key:str)->int:
    '''
    hash will hashed the key means convert the key string into a value of int
    parameters:
        key: a string
    Arguments: key
    Returns: Index in the collection for that key
    '''

    value=0
    for x in key:
      value += ord(x)
    index = (value * 7) % self.size
    return index


  def add(self,key,value):
    '''add a value to the hashtable by its key
    parameters:
        key: a string
        value: any type
    Arrgument: key and value
    return: nothing

    '''

    index = self.hash(key)

    if not self._buckets[index]:
      self._buckets[index] = LinkedList()


    self._buckets[index].append([key,value])



  def find(self,key):
    """this function will search in the hashtable about the key and return the value
    parameters:
      key: a string
    return: the value
      """
    index = self.hash(key)
    if self._buckets[index]:
            cuurrent=self._buckets[index].head
            while cuurrent:
                if cuurrent.value[0]==key:
                    print(cuurrent.value[1])
                    return cuurrent.value[1]
                cuurrent=cuurrent.next
    else:
        return None



  def contains(self,key):
    """this function will check if the there is a value for the key
    parameters:
      key: a string
    return: a boolean
    """
    index=self.hash(key)
    if self._buckets[index]:
      return self._buckets[index].includes(key)
    else:
      return False

ht=HashTable()
print(ht.hash("roaa"))
