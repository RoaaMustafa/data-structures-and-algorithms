import pytest
from linked_list import __version__
from linked_list.linked_list import LinkedList, Node


def test_version():
    assert __version__ == '0.1.0'

def test_create_Node():
  assert Node()

def test_value_in_node():
  node = Node("Test")
  actual = node.value
  assert actual == "Test"

def test_attributes_in_node():
  node = Node("Hi")
  actual = node.next
  assert True

def test_linkedlist():
   assert LinkedList()

def test_insert():

  ll = LinkedList()
  with pytest.raises(AttributeError):
    ll.head.value
  ll.insert(5)
  actual = ll.head.value
  assert actual == 5

def test_fined_value_linked_list():
    new_linked= LinkedList()
    new_linked.insert(5)
    assert new_linked.includes(5)


def test_fined_value_linked_list():
    new_linked= LinkedList()
    with pytest.raises(AttributeError):
        new_linked.head.value
    new_linked.insert(5)
    assert new_linked.includes(3)==False


def test_append_list():
    new_linked= LinkedList()
    new_linked.append(10)
    assert new_linked.includes(10)


def test_insert_on_last_list():
    new_linked= LinkedList()
    new_linked.append(10)
    new_linked.append(15)
    new_linked.append(26)

def test_insert_to_middle():
    new_linked= LinkedList()
    new_linked.insert(5)
    new_linked.insert(15)
    new_linked.insert(45)
    new_linked.insert(666)
    new_linked.insert_before(7,17)
    assert new_linked.includes(17)


def test_insert_befor_the_first():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(4)
    new_linked.insert(14)
    new_linked.insert(114)
    new_linked.insert_before(114,14)
    assert new_linked.includes(14)
def test_add_after_middle():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(8)
    new_linked.insert(2)
    new_linked.insert(114)
    new_linked.insert_after(114,30)
    assert new_linked.includes(30)
def test_add_after_last():
    new_linked= LinkedList()
    new_linked.insert(4)
    new_linked.insert(3)
    new_linked.insert(2)
    new_linked.insert(33)
    new_linked.insert_after(3,10)
    assert new_linked.includes(10)
