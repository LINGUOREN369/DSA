class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)

        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, current, data):
        if current is None:
            return False
        if current.data == data:
            return True
        if data < current.data:
            self._search_recursive(current.left, data)
        else:
            self._search_recursive(current.right, data)

        