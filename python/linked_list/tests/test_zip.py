import pytest
from linked_list.linked_list import LinkedList, Node
from  linked_list.linked_list import *

# def test_lists_zip():
#     ziplist=LinkedList()
#     llist1 = LinkedList()
#     llist2 = LinkedList()
#     llist1.append(1)
#     llist1.append(3)
#     llist1.append(5)
#     llist2.append(2)
#     llist2.append(4)
#     llist2.append(6)
#     actual =str(zipLists(llist1,llist2))
#     expected = "1-> 2-> 3-> 4-> 5-> 6-> None"
#     assert actual == expected
def test_zip_Lists():
    llist1 = LinkedList()
    llist1.append(1)
    llist1.append(2)
    llist1.append(3)
    llist2 = LinkedList()
    llist2.append('a')
    llist2.append('b')
    llist2.append('c')
    assert zipLists(llist1,llist2) == "1-> a-> 2-> b-> 3-> c-> None"
def test_zip_Lists2():
    llist1 = LinkedList()
    llist1.append(1)
    llist1.append(2)
    llist1.append(3)
    llist1.append(0)
    llist2 = LinkedList()
    llist2.append('a')
    llist2.append('b')
    llist2.append('c')
    assert zipLists(llist1,llist2) == "1-> a-> 2-> b-> 3-> c-> 0-> None"
