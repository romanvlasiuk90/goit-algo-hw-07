class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_sum(root):
    if root is None:
        return 0
    return root.val + find_sum(root.left) + find_sum(root.right)

# Приклад використання
root = TreeNode(10)
root = insert(root, 2)
root = insert(root, 5)
root = insert(root, 1)
root = insert(root, 7)

print("Сума всіх значень у дереві:", find_sum(root))