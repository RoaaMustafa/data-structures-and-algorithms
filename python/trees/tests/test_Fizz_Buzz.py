import pytest
from trees.tree_Fizz_Buzz import *


@pytest.fixture
def data():

    tree = k_ary_tree()
    tree.root = Node(3)

    tree.root.children.append(Node(2))
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(15))

    tree.root.children[0].children.append(Node(4))
    tree.root.children[0].children.append(Node(6))
    tree.root.children[0].children.append(Node(7))

    tree.root.children[1].children.append(Node(9))
    tree.root.children[1].children.append(Node(18))
    tree.root.children[2].children.append(Node(45))


    return tree


def test_if_fizz(data):
    new_tree =  fizz_buzz_tree(data)
    actual=new_tree.root.value
    expected='Fizz'
    assert actual==expected

def test_if_Buzz(data):
    new_tree =  fizz_buzz_tree(data)
    actual=new_tree.root.children[1].value
    expected='Buzz'
    assert actual==expected

def test_if_fizzBuzz(data):
    new_tree =  fizz_buzz_tree(data)
    actual=new_tree.root.children[2].value
    expected='FizzBuzz'
    assert actual==expected

def test_raise():
    x=None
    with pytest.raises(ValueError, match="Empty Root"):
     new_tree =  fizz_buzz_tree(x)
