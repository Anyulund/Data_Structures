#Binary tree

class Node:
    def __init__ (self,value):
        self.data = value
        self.left = None
        self.right = None

    def insert (self,value):
        if value == self.data:
            return False
        elif value < self.data:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
        elif value > self.data:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)

    def in_order(self, n_list):
        if self.left:
            self.left.in_order(n_list)
        n_list.append(self.data)
        if self.right:
            self.right.in_order(n_list)
        return n_list

    def pre_order(self, n_list):
        n_list.append(self.data)
        if self.left:
            self.left.pre_order(n_list)
        if self.right:
            self.right.pre_order(n_list)
        return n_list

    def post_order(self, n_list):
        if self.left:
            self.left.post_order(n_list)
        if self.right:
            self.right.post_order(n_list)
        n_list.append(self.data)
        return n_list

    def height(self,n_node):
        if n_node:
            left_d = self.height(n_node.left)
            right_d = self.height(n_node.right)
            if left_d < right_d:
                return right_d +1
            else:
                return left_d +1
        else:
            return 0

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data and self.left:
            return self.left.contains(value)
        elif value > self.data and self.right:
            return self.right.contains(value)
        else:
            return False

class Tree:

    # 1) Write a function that takes in a list of integers, creates a binary tree with those integers
    def __init__(self, values):
      self.root = None
      for value in values:
          if self.root:
              self.root.insert(value)
          else:
              self.root = Node(value)

    # 2) Write a function that raeturns the in-order traversal of the tree as space-separated string.
    def in_order(self):
        if self.root:
            return self.root.in_order([])
        else:
            return []

    # 3) Write a function that returns the pre-order traversal of the tree as space-separated string.
    def pre_order(self):
        if self.root:
            return self.root.pre_order([])
        else:
            return []

    # 4) Write a function that returns the post-order traversal of the tree as space-separated string.
    def post_order(self):
        if self.root:
            return self.root.post_order([])
        else:
            return []

    # 5) Write a function that determines the height of a given tree.
    def height(self):
        if self.root:
            return self.root.height(self.root)
        else:
            return 0

    # 6) Write a function that returns the sum of all values in a tree.
    def sum(self):
        n_values = self.root.in_order([])
        #print(n_values)
        total = 0
        for n_value in n_values:
            total += n_value
        return total

    # 7) Write a function that returns a bool indicating that a value exists (or not) in a given tree.
    def contains(self, value):
        if self.root:
            return self.root.contains(value)

treeList = [10, 15, 7, 9, 3, 24]
palm_tree = Tree(treeList)
print(palm_tree.in_order())
print(palm_tree.pre_order ())
print(palm_tree.post_order ())
print(palm_tree.height())
print(palm_tree.sum())
print(palm_tree.contains(10))
