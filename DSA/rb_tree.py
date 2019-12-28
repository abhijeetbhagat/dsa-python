# RBTree implementation based on these YT videos
# https://www.youtube.com/watch?v=UaLIHuR1t8Q 
# https://www.youtube.com/playlist?list=PL9xmBV_5YoZNqDI8qfOZgzbqahCUmUEin

from enum import Enum

class RBTree:
    class Color(Enum):
        RED = 1,
        BLACK = 2,
        NONE = 3

    class Node:
        def __init__(self, parent, left, right, val, color):
            self.parent = parent
            self.left = left
            self.right = right
            self.val = val
            self.color = color

    def __init__(self):
        self.root = None


    def get_parent(node: Node):
        if node is None:
            return None

        return node.parent


    def get_grand_parent(node: Node):
        return RBTree.get_parent(RBTree.get_parent(node))


    def get_sibling(node: Node):
        if node is None:
            return None

        parent = RBTree.get_parent(node)
        if parent is None:
            return None

        if node == parent.left:
            return node.right
        else:
            return node.left


    def get_parents_sibling(node: Node):
        parent = RBTree.get_parent(node)
        grandpa = RBTree.get_grand_parent(node)
        if parent == grandpa.left:
            return grandpa.right
        else:
            return grandpa.left


    def insert(self, val):
        # if the tree is empty, then just
        # create a black root node and return
        if self.root is None:
            self.root = RBTree.Node(None, None, None, val, RBTree.Color.BLACK)
            return

        # we insert the new node as a red node since
        # a leaf is always red; so create one
        z = RBTree.Node(None, None, None, val, RBTree.Color.RED)

        # find the right place to insert the new node
        # in the BST (rb tree is a BST)
        ptr = self.root
        ptr2 = None
        while ptr is not None:
            ptr2 = ptr
            if z.val < ptr.val:
                ptr = ptr.left
            else:
                ptr = ptr.right

        if z.val < ptr2.val:
            ptr2.left = z
        else:
            ptr2.right = z

        # set new node's parent
        z.parent = ptr2

        # if the parent of the newly inserted
        # node is black, then just
        # return coz we are done
        # otherwise, run this loop because
        # violations will be propagated up the tree
        # while fixing them
        parent = RBTree.get_parent(z)
        while RBTree.get_parent(z).color != RBTree.Color.BLACK:
            # we are violating the
            # red-red parent-child relationship
            
            # To fix this violation, first get
            # parent's sibling (uncle) -
            uncle = RBTree.get_parents_sibling(z)
            # if there's no uncle, then it is assumed to be
            # a black NIL node
            uncle_color = RBTree.Color.BLACK if uncle is None else uncle.color

            grandpa = RBTree.get_grand_parent(z)
            # If uncle is red, then flip the color of
            # parent and uncle to black
            if uncle_color == RBTree.Color.RED:
                RBTree.flip_color(parent)
                RBTree.flip_color(uncle)
                # If node's grandpa is root then we are done
                if grandpa == self.root:
                    return
                # otherwise, we flip grandpa's color
                else:
                    RBTree.flip_color(grandpa)
                z = grandpa
                parent = RBTree.get_parent(z)
            # otherwise, uncle is black
            else:
                # time for rotations!
                # Check what kind of a formation our new
                # node is in - line or triangle - and then
                # rotate either the parent or the grand-parent
                if parent == grandpa.left and z == parent.left: # line
                    # rotate grand-parent to the right (opposite direction of z)
                    root = RBTree.rotate_right(grandpa)
                    if root is not None:
                        self.root = root
                    # flip colors of node's parent and parent's right child
                    RBTree.flip_color(parent)
                    RBTree.flip_color(parent.right)
                elif parent == grandpa.right and z == parent.right: # line
                    # rotate grand-parent to the left (opposite direction of z)
                    root = RBTree.rotate_left(grandpa)
                    if root is not None:
                        self.root = root
                    # flip colors of node's parent and parent's left child
                    RBTree.flip_color(parent)
                    RBTree.flip_color(parent.left)
                elif parent == grandpa.left and z == parent.right: # triangle
                    # rotate parent to the left
                    RBTree.rotate_left(parent)
                    # rotate grandpa to the right
                    RBTree.rotate_right(grandpa)
                    # flip colors of parent and grandpa
                    RBTree.flip_color(z)
                    RBTree.flip_color(z.right)
                else: # parent is grandpa's right and z is parent's left; so, triangle
                    # rotate parent to the right
                    RBTree.rotate_right(parent)
                    # rotate grandpa to the left
                    RBTree.rotate_left(grandpa)
                    # flip colors of parent and grandpa
                    RBTree.flip_color(z)
                    RBTree.flip_color(z.left)


    # rotates a given node to the left
    def rotate_left(node):
        # get parent of the node at which rotation
        # is to be done
        parent = RBTree.get_parent(node)

        root = None
        # detach the node from its parent and
        # attach node's right child in its place
        if parent is not None:
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            root = node.right

        # store node's left child's left child
        left_child = None
        if node.right is not None:
            left_child = node.right.left

        # node's right child now becomes its
        # parent and node attaches as a left child
        node.right.parent = parent
        node.right.left = node
        node.parent = node.right

        # attach node's new parent's former left child
        # as node's right child
        node.right = left_child

        return root


    # rotates a given node to the right
    def rotate_right(node):
        # get parent of the node at which rotation
        # is to be done
        parent = RBTree.get_parent(node)

        root = None
        # detach the node from its parent and
        # attach node's left child in its place
        if parent is not None:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            root = node.left

        # store node's left child's right child
        # in a temp
        right_child = None
        if node.left is not None:
            right_child = node.left.right
        # node's left child now becomes its
        # parent, node's left child's parent now
        # becomes node's parent and node attaches as a right child
        node.left.parent = parent
        node.left.right = node
        node.parent = node.left

        # attach node's new parent's former right child
        # as node's left child
        node.left = right_child

        return root


    # changes a color of the given node from black to red
    # and vice-versa
    def flip_color(node):
        node.color = RBTree.Color.BLACK if node.color == RBTree.Color.RED else RBTree.Color.RED


    def delete(self, val):
        pass

    def print_inorder(self):
        RBTree.__inorder_traverse(self.root)

    def __inorder_traverse(node: Node):
        if node is not None:
            RBTree.__inorder_traverse(node.left)
            print(f"{node.val}:{node.color}", end=' ')
            RBTree.__inorder_traverse(node.right)

'''
tree = RBTree()
tree.insert(15)
tree.insert(5)
tree.insert(1)
tree.print_inorder()
print()

tree = RBTree()
tree.insert(10)
tree.insert(20)
tree.insert(-10)
tree.print_inorder()
print()
tree.insert(15)
tree.print_inorder()
print()
tree.insert(17)
tree.print_inorder()
print()
tree.insert(40)
tree.print_inorder()
print()
tree.insert(50)
tree.print_inorder()
print()
tree.insert(60)
tree.print_inorder()
print()
'''

tree = RBTree()
tree.insert(10)
tree.insert(9)
tree.insert(8)
tree.print_inorder()
print()
tree.insert(7)
tree.print_inorder()
print()
tree.insert(6)
tree.print_inorder()
print()
tree.insert(5)
tree.print_inorder()
print()
tree.insert(4)
tree.print_inorder()
print()
tree.insert(3)
tree.insert(2)
tree.insert(1)
tree.print_inorder()
print()
