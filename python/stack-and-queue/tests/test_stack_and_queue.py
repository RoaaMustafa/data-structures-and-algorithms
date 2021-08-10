
import pytest
from stack_and_queue import __version__
from stack_and_queue.stack_and_queue import Stack,Node,Queue
from stack_and_queue.stack_queue_pseudo import Pseudo_queue
from stack_and_queue.stack_queue_animal_shelter import *
from stack_and_queue.stack_queue_brackets import *

def test_version():
    assert __version__ == '0.1.0'

def test_instance_node():
  assert Node()

def test_if_node_has_vlaue():
  node = Node("Test")
  actual = node.value
  assert actual == "Test"

def test_node_has_next_property():
  node = Node("test")
  actual = node.next
  assert True

# def test_empty_stack():
#     assert Stack()

def test_has_one_node():
    test=Stack()
    test.push(1)
    expected=1
    actual=test.peek()
    assert expected==actual

def test_insert_more_nodes():
    test=Stack()
    test.push(0)
    test.push(1)
    test.push(2)
    expected=3
    actual=test.__len__()
    assert expected==actual

def test_remove_node():
    test=Stack()
    test.push(0)
    test.push(1)
    test.push(1)
    test.pop()
    expected=1
    actual=test.peek()
    assert expected==actual

def test_stack_is_empty():
  test = Stack()
  assert test.is_empty()

def test_stack_not_empty():
  test = Stack()
  test.push(1)
  assert not test.is_empty()

def test_is_empty_for_peek_and_pop():
    test=Stack()
    with pytest.raises(Exception, match="empty stack"):
         test.peek()
         test.pop()





def test_has_one_node_queueu():
    test=Queue()
    test.enqueue(0)
    expected=0
    actual=test.peek()
    assert expected==actual

def test_insert_more_nodes_queueu():
    test=Queue()
    test.enqueue(0)
    test.enqueue(1)
    test.enqueue(1)
    expected=3
    actual=test.__len__()
    assert expected==actual

def test_remove_node_queueu():
    test=Queue()
    test.enqueue(0)
    test.enqueue(1)
    test.enqueue(1)
    test.dequeue()
    expected=1
    actual=test.peek()
    assert expected==actual

def test_stack_is_empty_queueu():
  test = Queue()
  assert test.is_empty()

def test_stack_not_empty_queueu():
  test = Queue()
  test.enqueue(1)
  assert not test.is_empty()

def test_is_empty_for_peek_and_pop_queueu():
    test=Queue()
    with pytest.raises(Exception, match="empty equeue"):
         test.peek()
         test.dequeue()



def test_pseudoqueue_dequeue(data):
    assert data.dequeue() == 10
    assert data.dequeue() == 15
    assert data.dequeue() == 20
    assert data.dequeue() == 5

def test_pseudoqueue_enqueue(data):
  assert data.push_stack.top.value==5
  assert data.push_stack.top.next.value==20
  assert data.push_stack.top.next.next.value==15
  assert data.push_stack.top.next.next.next.value==10

@pytest.fixture
def data():
    queue = Pseudo_queue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue(5)
    return queue




# //////////////////////////


def test_Animal_Shelter_dequeue(data):
    assert data.dequeue('cat') == 'cat'
    assert data.dequeue('cat') == 'cat'
    assert data.dequeue('dog') == 'dog'
    assert data.dequeue('dog') == 'dog'
    assert data.dequeue('dog') == 'The animal not there'
    assert data.dequeue('cat') == 'The animal not there'
    assert data.dequeue('bird') == 'The animal not in the shelf for ignore it'

def test_Animal_Shelter_enqueue(data):
    assert data.cat.front.value=='cat'
    assert data.cat.front.next.value=='cat'
    assert data.dog.front.value=='dog'
    assert data.dog.front.next.value=='dog'
    assert data.enqueue('hh')=='The animal is not in the list'





@pytest.fixture
def data():
    my_queue = AnimalShelter()
    my_queue.enqueue('cat')
    my_queue.enqueue('cat')
    my_queue.enqueue('dog')
    my_queue.enqueue('dog')
    return my_queue
# ///////////////////////////////////////////////
def test_validate_one_open_bracket():
    test="("
    expected=False
    actual=validatee_brackets(test)
    assert expected==actual

def test_validate_one_close_bracket():
    test=")"
    expected=False
    actual=validatee_brackets(test)
    assert expected==actual

def test_validate_one_open_And_one_close_bracket():
    test="()"
    expected=True
    actual=validatee_brackets(test)
    assert expected==actual

def test_validate_multiple_brackets():
    test="[(){}[]]"
    expected=True
    actual=validatee_brackets(test)
    assert expected==actual

def test_validate_multiple_brackets_with_String():
    test="hjk[(hkj){hkj}[hjk]hjbk]"
    expected=True
    actual=validatee_brackets(test)
    assert expected==actual
