class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.arr = []

    def pre_order(self, root):
        try:
            self.arr.append(root.value)
            if root.left != None:
                self.pre_order(root.left)

            if root.right != None:
                self.pre_order(root.right)
            return self.arr
        except:
            raise Exception("Error  with pre_order ")

    def in_order(self, root):
        try:
            if root.left:
                self.in_order(root.left)

            self.arr.append(root.value)

            if root.right:
                self.in_order(root.right)

            return self.arr
        except:
            raise Exception("Error  with in_order")

    def test(self):
        self.arr = []

    def post_order(self, root):
        try:
            if root.left:
                self.post_order(root.left)

            if root.right:
                self.post_order(root.right)

            self.arr.append(root.value)
            return self.arr
        except:
            raise Exception("Error  with post_order")



class BinarySearch(BinaryTree):

    def add(self, value):

        if not self.root:
            self.root = Node(value)
            # print(self.root.value)
            return

        current = self.root

        while current:
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)

                    return

            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return

    def Contains(self, value):

        if not self.root:
            raise Exception("empty is tree")
        elif value == self.root.value:
            return True
        else:
            current = self.root
            while current:

                if current.value < value:

                    if current.right:
                        current = current.right
                        if value == current.value:
                            return True
                    else:
                        return False

                else:

                    if current.left:
                        current = current.left
                        if value == current.value:
                            return True
                    else:
                        return False

# my_search=BinaryTree()
# my_search.root=Node("A")
# my_search.left=Node("B")
# my_search.right=Node("C")
# my_search.left.left=Node("D")
# my_search.left.right=Node("E")
# my_search.right.left=Node("F")
# print(my_search)


