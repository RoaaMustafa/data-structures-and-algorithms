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
