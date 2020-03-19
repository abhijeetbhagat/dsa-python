class BST:
    class Node:
        def __init__(self, left, right, val):
            self.left = left
            self.right = right
            self.val = val

    def __init__(self):
        self.root = None

    
    def insert(self, val):
        if self.root == None:
            self.root = BST.Node(None, None, val)
            return

        new_node = BST.Node(None, None, val)
        
        ptr = self.root
        ptr2 = None
        while ptr != None:
            ptr2 = ptr 
            if new_node.val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right 

        if new_node.val < ptr2.val:
            ptr2.left = new_node 
        else:
            ptr2.right = new_node 

    
    def delete(self):
        pass


    def inorder_successor(self, key):
        node = self.search(key)
        r =  BST.__inorder_succ(node.right)
        return r


    def __inorder_succ(node):
        if node is not None:
            BST.__inorder_succ(node.left)
            return node.val

    
    def search(self, key):
        return BST.__search(self.root, key)

    def __search(node, key):
        if node is not None:
            if key < node.val:
                return BST.__search(node.left, key)
            elif key > node.val:
                return BST.__search(node.right, key)
            else:
                return node
        else:
            return None


    def inorder_predeccessor(self):
        pass


bst = BST()
bst.insert(5)
bst.insert(8)
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(3)
assert(bst.search(5) is not None)
assert(bst.search(2) is not None)
assert(bst.search(1) is not None)
assert(bst.search(4) is not None)
assert(bst.search(3) is not None)
assert(bst.search(8) is not None)
assert(bst.search(9) is None)
assert(bst.inorder_successor(5) == 8)
assert(bst.inorder_successor(2) == 4)
assert(bst.inorder_successor(1) == 2)