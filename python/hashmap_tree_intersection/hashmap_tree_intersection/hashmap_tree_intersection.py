from hashmap_tree_intersection.hashtable import *
from hashmap_tree_intersection.tree import *


def intersection(tree1,tree2):
    """
    Write a function called tree intersection
    Arguments: two binary trees
    Return: array

    """
    arr=[]
    hashtable=Hash_table(1024)

    if tree1.root==None or tree2.root==None:
        return 'one of the tree is empty'

    def travers(node):
        if hashtable.contains(str(node.value)):
            nonlocal arr
            arr+=[node.value]
        else:
            hashtable.add(str(node.value),True)

        if node.left:
            travers(node.left)
        if node.right:
            travers(node.right)
    travers(tree1.root)
    travers(tree2.root)

    return arr







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
# print(tree1.in_order(root1))
print(intersection(tree1,tree2))
