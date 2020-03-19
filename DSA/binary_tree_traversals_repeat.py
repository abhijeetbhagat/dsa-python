class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.value)
        in_order(node.right)

def pre_order(node):
    if node is not None:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.value)

def level_order(node):
    pass

n = Node(Node(None, None, 2), Node(None, None, 3), 1)
print("In order:")
in_order(n)
print("Pre order:")
pre_order(n)
print("Post order:")
post_order(n)

