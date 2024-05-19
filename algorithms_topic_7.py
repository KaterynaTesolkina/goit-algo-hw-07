# Завдання 1

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root 

def find_max_value(root):
    if root is None:
        return None
    
    while root.right is not None:
        root = root.right
    
    return root.val

# Test
root = Node(5)
root = insert(root, 3) # type: ignore
root = insert(root, 2) # type: ignore
root = insert(root, 4) # type: ignore
root = insert(root, 7) # type: ignore
root = insert(root, 6) # type: ignore
root = insert(root, 8) # type: ignore

# Знаходження максимального значення
max_value = find_max_value(root)
print(f"Максимальне значення в дереві: {max_value}")

# Завдання 2
def find_min_value(root):
    if root is None:
        return None
    
    while root.left is not None:
        root = root.left
    
    return root.val

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

# Знаходження найменшого значення
min_value = find_min_value(root)
print(f"Найменше значення в дереві: {min_value}")

# Завдання 3
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def sum_of_values(node):
    if node is None:
        return 0
    return node.key + sum_of_values(node.left) + sum_of_values(node.right)

# Test
root = None
keys = [10, 20, 5, 6, 15, 30, 25, 35]

for key in keys:
    root = insert(root, key)

print(f"Cума всіх значень: {sum_of_values(root)}")
