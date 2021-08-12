class Node:
   def __init__(self,value):
      self.value= value
      self.left=None
      self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    # def pre_order(self,root):
    #    output = []
    #     #  print(f"OUTPUT <-- {root.value}")
    #    try:
    #     if not self.root:
    #      return output
    #     if root.left is not None:
    #       pre_order(root.left)

    #     if root.right is not None:
    #      pre_order(root.right)
    #    except:
    #         raise Exception("Error with insertion by pre_order")

    # def in_order(self ,root):
    #     output = []
    #     try:
    #      if not self.root:
    #       return output
    #      if root.left is not None:
    #       in_order(root.left)

    #      output.append(root.value)

    #      if root.right is not None:
    #       in_order(root.right)
    #     except:
    #      raise Exception("Error with insertion by in_order")

    # def post_order(self,root):
    #     output = []
    #     try:
    #       if not self.root:
    #        return output
    #       if root.left is not None:
    #        post_order(root.left)

    #       if root.right is not None:
    #        post_order(root.right)

    #       output.append(root.value)
    #     except:
    #      raise Exception("Error with insertion by post_order")
    def in_order(self, node=None, results=None):
        node = node or self.root
        results = results or []
        if node:
            if node.left:
                self.in_order(node.left, results)
            results.append(node.value)
            if node.right:
                self.in_order(node.right, results)
        return results

    def pre_order(self, node=None, results=None):
        node = node or self.root
        results = results or []
        if node:
            results.append(node.value)
            if node.left:
                self.pre_order(node.left, results)
            if node.right:
                self.pre_order(node.right, results)
        return results

    def post_order(self, node=None, results=None):
        node = node or self.root
        results = results or []
        if node:
            if node.left:
                self.post_order(node.left, results)
            if node.right:
                self.post_order(node.right, results)
            results.append(node.value)
        return results


class BinarySearchTree(BinaryTree):
    def add(self, value, root=None):
        root = root or self.root
        node = Node(value)
        if not self.root:
            self.root = node
            return
        if value < root.value:
            if root.left:
                self.add(value, root.left)
            else:
                root.left = node
        else:
            if root.right:
                self.add(value, root.left)
            else:
                root.right = node

    def contains(self, value, current=None):
        current = current or self.root
        if not self.root or value == None:
            print('no')
            return False
        if current.value == value:
            print('yes')
            return True
        elif current.value < value:
            return self.contains(value, current.left)
        else:
            return self.contains(value, current.right)
        print('no')
        return False


my_search=BinaryTree()
root=Node("A")
root.left=Node("B")
root.right=Node("C")
root.left.left=Node("D")
root.left.right=Node("E")
root.right.left=Node("F")
print(root)


