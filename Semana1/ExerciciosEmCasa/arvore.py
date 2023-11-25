class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.key, end=' ')
        in_order_traversal(root.right)

def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return 1 + max(left_height, right_height)

def is_balanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True

    return False

keys = [10, 5, 15, 3, 7, 12, 20, 2, 4, 6, 8]
bst_root = None

for key in keys:
    bst_root = insert(bst_root, key)

print("In-Order Traversal:")
in_order_traversal(bst_root)
print("\n")

if is_balanced(bst_root):
    print("A árvore é balanceada.")
else:
    print("A árvore não é balanceada.")
