import re
from hashmap_repeated_word.linked_list import *
from hashmap_repeated_word.hashtable import *


# def repeated_word(book=None):
#     if book == None :
#         return 'the book is empty'
#     hash_table = HashTable(1024)

#     book = re.sub('\W+', ' ', book).lower().split()

#     for word in book:

#         if hash_table.contains(word):
#             return word
#         else:

#             hash_table.add(word, True)

def repeated_word(sentance=None):
    arr=sentance.lower().split(" ")
    hash_table=HashTable()
    if sentance == None :
        return "None"
    for  i in arr:
        if hash_table.contains(i):
            return (i, len(arr))
        hash_table.add(i,i)
    return "None"

if __name__ == "__main__":

    book="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."

    print(repeated_word(book))
