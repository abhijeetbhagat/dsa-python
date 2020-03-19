import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryHorizontalDistance:
    def find_distance(self, node, n1, n2):
        left_node_to_root = self._path_length(node, n1, "left_node_to_root") - 2
        right_node_to_root = self._path_length(node, n2, "right_node_to_root") - 2
        lca_data = self._find_lca(node, n1, n2).data
        lca_distance = self._path_length(node, lca_data, "lca_distance") - 1
        return left_node_to_root + right_node_to_root - 2 * lca_distance


    def _path_length(self, root, n, calling_from):
        if root is not None:
            x = 0
            string = None
            if calling_from == "right_node_to_root":
                string = "right_node_to_root"
            else:
                string = "left_node_to_root"

            if root.data == n:
                return x + 1
            else:
                x = self._path_length(root.left, n, string)
                if x > 0:
                    return x + 1
                x = self._path_length(root.right, n, string)
                if x > 0:
                    return x + 1

        return 0


    def _find_lca(self, root: Node, n1, n2):
        if root is not None:
            if root.data == n1 or root.data == n2:
                return root

            left = self._find_lca(root.left, n1, n2)
            right = self._find_lca(root.right, n1, n2)

            if left is not None and right is not None:
                return root
            elif left is not None:
                return root.left
            else:
                return root.right

        return None


class BinaryHorizontalDistanceTests(unittest.TestCase):
    def test_distances(self):
        root = Node(5);
        root.right = Node(3);
        root.left = Node(2);
        root.right.right = Node(1);
        root.right.right.right = Node(6);
        root.left.left = Node(7);
        # root.right.right.left = Node(4);
        root.left.left.left = Node(9);

        binaryTree = BinaryHorizontalDistance();
        self.assertEqual(binaryTree.find_distance(root, 7, 1), 2)
        self.assertEqual(binaryTree.find_distance(root, 9, 6), 4)


if __name__ == "__main__":
    unittest.main()
