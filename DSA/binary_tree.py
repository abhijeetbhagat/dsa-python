class Node:
    def __init__(self, val):
        self.right = None
        self.left  = None
        self.value = val

def inorder(node : Node):
    if node is not None:
        inorder(node.left)
        print(node.value, end = ' ')
        inorder(node.right)

def preorder(node : Node):
    if node is not None:
        print(node.value, end = ' ')
        preorder(node.left)
        preorder(node.right)

from collections import deque
def levelorder(node : Node):
    if node is None:
        return
    q = deque()
    q.append(node)
    while q :
        n = q.popleft()
        print(n.value, end = ' ')
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)

def height(node : Node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)

#inorder(root)
#print()
#preorder(root)
#print()
levelorder(root)
print()
print(height(root))