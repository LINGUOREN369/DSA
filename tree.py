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
        if data <  current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

    def inorder_traversal(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements
    
    def _inorder_recursive(self, current, elements):
       if current:
           self._inorder_recursive(current.left, elements)
           elements.append(current.data)
           self._inorder_recursive(current.right, elements)

    def preorder_traversal(self):
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements 
    
    def _preorder_recursive(self, current, elements):
        if current:
            elements.append(current.data)
            self._preorder_recursive(current.left, elements)
            self._preorder_recursive(current.right, elements)

    def postorder_traversal(self):
        elements = []
        self._postorder_recursive(self.root, elements)
        return elements 
    
    def _postorder_recursive(self, current, elements):
        if current:
            self._postorder_recursive(current.left, elements)
            self._postorder_recursive(current.right, elements)
            elements.append(current.data)

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(3)
    bt.insert(7)
    bt.insert(13)
    bt.insert(18)

    print("Inorder traversal:", bt.inorder_traversal())  # Output: [3, 5, 7, 10, 13, 15, 18]
    print("Preorder traversal:", bt.preorder_traversal())  # Output: [10, 5, 3, 7, 15, 13, 18]
    print("Postorder traversal:", bt.postorder_traversal())  # Output: [3, 7, 5, 13, 18, 15, 10]
    print("Search 7:", bt.search(7))  # Output: True
    print("Search 8:", bt.search(8))  # Output: False