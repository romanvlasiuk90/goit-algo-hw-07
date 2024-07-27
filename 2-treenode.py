# Двійкове дерево пошуку (BST)
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

def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

root = TreeNode(10)
root = insert(root, 20)
root = insert(root, 5)
root = insert(root, 9)
root = insert(root, 7)

print("Найменше значення в дереві:", find_min(root))