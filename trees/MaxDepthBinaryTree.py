from common.TreeNode import TreeNode


class Solver:
    """
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

    Note: A leaf is a node with no children.

    Example:

    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its depth = 3.
    """
    def max_depth(self, root):
        if not root:
            return 0

        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


def main():
    solver = Solver()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(solver.max_depth(root))


if __name__ == "__main__":
    main()
