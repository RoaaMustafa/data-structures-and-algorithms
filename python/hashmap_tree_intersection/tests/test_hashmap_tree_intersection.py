from hashmap_tree_intersection import __version__
from hashmap_tree_intersection.hashtable import *
from hashmap_tree_intersection.tree import *
from hashmap_tree_intersection.hashmap_tree_intersection import *

def test_version():
    assert __version__ == '0.1.0'



def test_tree_intersection():
    tree1=BinaryTree()
    root1=Node(100)
    root1.left=Node(200)
    root1.left.left=Node(300)
    root1.left.right=Node(400)
    root1.right=Node(500)
    root1.right.left=Node(600)
    tree1.root=root1

    tree2=BinaryTree()
    root=Node(100)
    root.left=Node(500)
    root.left.left=Node(1000)
    root.left.right=Node(600)
    root.right=Node(687)
    root.right.left=Node(7689)
    root.right.left.left=Node(300)

    tree2.root=root

    assert intersection(tree1,tree2)==[100,500,600,300]


def test_tree_intersection_if_no_intersection():
    tree1=BinaryTree()
    root1=Node(10570)
    root1.left=Node(20089)
    root1.left.left=Node(30980)
    root1.left.right=Node(49800)
    root1.right=Node(50890)
    root1.right.left=Node(60090)
    tree1.root=root1

    tree2=BinaryTree()
    root=Node(100)
    root.left=Node(500)
    root.left.left=Node(1000)
    root.left.right=Node(600)
    root.right=Node(687)
    root.right.left=Node(7689)
    root.right.left.left=Node(300)

    tree2.root=root

    assert intersection(tree1,tree2)==[]
