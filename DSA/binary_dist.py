class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryHorizontalDistance:
    def __init__(self):
        pass

    def find_distance(self, node: Node, n1, n2) -> int:
        left_node_to_root = self.path_length(node, n1, "left_node_to_root") - 2
        right_node_to_root = self.path_length(node, n2, "right_node_to_root") - 2
        lca_data = self.find_lca(node, n1, n2).data
        lca_distance = self.path_length(node, lca_data, "lca_distance") - 1
        return left_node_to_root + right_node_to_root - 2 * lca_distance

    def path_length(self, root: Node, n1, calling_from: str) -> int:
        if root is not None:
            x = 0
            string = None
            if calling_from == "right_node_to_root":
                if root.left is None and root.right is None:
                    pass
                elif root.left is None or root.right is None:
                    print(f"counting the position where the node is not present is {root.data}")

                string = "right_node_to_root"

            else:
                string = "left_node_to_root"

            if root.data == n1:
                return x + 1
            else:
                x = self.path_length(root.left, n1, string)
                if x > 0:
                    return x + 1
                x = self.path_length(root.right, n1, string)
                if x > 0:
                    return x + 1

        return 0


    def find_lca(self, root: Node, n1, n2) -> Node:
        if root is not None:
            if root.data == n1 or root.data == n2:
                return root

            left = self.find_lca(root.left, n1, n2)
            right = self.find_lca(root.right, n1, n2)

            if left is not None and right is not None:
                return root
            elif left is not None:
                return root.left
            else:
                return root.right

        return None

if __name__ == "__main__":
    root = Node(5);
    root.right = Node(3);
    root.left = Node(2);
    root.right.right = Node(1);
    root.right.right.right = Node(6);
    root.left.left = Node(7);
    root.right.right.left = Node(4);
    root.left.left.left = Node(9);

    binaryTreeTest = BinaryHorizontalDistance();
    print(f"Distance between 7 and 1 is : {binaryTreeTest.find_distance(root,7, 1)}");
    print(f"Distance between 9 and 6 is : {binaryTreeTest.find_distance(root,9, 6)}");
