class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, start, new_val):
        if start.value > new_val:
            if start.left:
                self.insert(start.left, new_val)
            else:
                start.left = Node(new_val)
        elif start.value < new_val:
            if start.right:
                self.insert(start.right, new_val)
            else:
                start.right = Node(new_val)


    def search(self, start, find_val):
        if start == None:
            return False
        if start.value == find_val:
            return True
        else:
            return self.search(start.left,find_val) or self.search(start.right,find_val)

###  reference

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(tree.root,2)
tree.insert(tree.root,1)
tree.insert(tree.root,3)
tree.insert(tree.root,5)

# Check search
# Should be True
print(tree.search(tree.root,4))

# Should be False
print(tree.search(tree.root,6))




class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
