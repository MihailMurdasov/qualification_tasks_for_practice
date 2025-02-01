class AVLNode:
    """
        Описывает узел АВЛ-дерева.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    """
        Возвращает высоту узла.
    """
    if not node:
        return 0
    return node.height

def update_height(node):
    """
        Обновляет высоту узла.
    """
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    """
        Возвращает баланс-фактор узла.
    """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def get_min_value_node(root):
    """
        Возвращает узел с минимальным значением.
    """
    if root is None or root.left is None:
        return root
    return get_min_value_node(root.left)

def get_max_value_node(root):
    """
        Возвращает узел с максимальным значением.
    """
    if root is None or root.right is None:
        return root
    return get_max_value_node(root.right)

def balance(node):
    """
        Выполняет балансировку узла.
    """
    if not node:
        return node

    balance_factor = get_balance(node)

    if balance_factor > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)

    if balance_factor > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance_factor < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    if balance_factor < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def right_rotate(z):
    """
        Выполняет правый поворот узла для балансировки дерева.
    """
    y = z.left
    t = y.right

    y.right = z
    z.left = t

    update_height(z)
    update_height(y)

    return y

def left_rotate(z):
    """
        Выполняет левый поворот узла для балансировки дерева.
    """
    y = z.right
    t = y.left

    y.left = z
    z.right = t

    update_height(z)
    update_height(y)

    return y

def insert(root, key):
    """
        Выполняет выставку нового узла в дерево.
    """
    if not root:
        return AVLNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)
    return balance(root)

def delete(root, key):
    """
        Выполняет удаление узла из дерева по значению key.
    """
    if search(root, key) is False:
        return None
    if not root:
        return root
    elif key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return  root.right
        elif root.right is None:
            return root.left

        temp = get_min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    if root is None:
        return root

    update_height(root)
    return balance(root)

def delete_min(root):
    """
        Выполняет удаление узла с минимальным значением.
    """
    if root is None:
        return root
    min_node = get_min_value_node(root)
    return delete(root, min_node.key)

def delete_max(root):
    """
        Выполняет удаление узла с максимальным значением.
    """
    if root is None:
        return root
    max_node = get_max_value_node(root)
    return delete(root, max_node.key)

def pre_order(node):
    """
        Выполняет pre-order обход дерева.
    """
    elements = []
    if node is not None:
        elements.append(node.key)
        elements += pre_order(node.left)
        elements += pre_order(node.right)

    return elements

def post_order(node):
    """
        Выполняет pre-order обход дерева.
    """
    elements = []
    if node is not None:
        elements += post_order(node.left)
        elements += post_order(node.right)
        elements.append(node.key)

    return elements

def in_order(node):
    """
        Выполняет in-order обход дерева.
    """
    elements = []
    if node is not None:
        elements += in_order(node.left)
        elements.append(node.key)
        elements += in_order(node.right)
    return elements

def search(node, key):
    """
        Выполняет поиск узла по значению key и возвращает True, если узел найден.
    """
    if node is None:
        return False
    if node.key == key:
        return True
    elif key < node.key:
        return search(node.left, key)
    elif key > node.key:
        return search(node.right, key)

def create_avl(elements):
    """
        Создает АВЛ-дерево из отсортированного массива элементов.
    """
    if not elements:
        return None
    mid = len(elements) // 2
    node = AVLNode(elements[mid])
    if len(elements) == 1:
        return node
    node.left = create_avl(elements[:mid])
    node.right = create_avl(elements[mid+1:])
    update_height(node)
    return balance(node)

def split(root, key):
    """
        Разделяет АВЛ-дерево на два других по значению key.
    """
    if search(root, key) is False:
        return None, None

    left_tree = []
    right_tree = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        if node.key < key:
            left_tree.append(node.key)
        else:
            right_tree.append(node.key)
        traverse(node.right)
    traverse(root)
    left_tree = sorted(left_tree)
    right_tree = sorted(right_tree)
    return create_avl(left_tree), create_avl(right_tree)

def merge(left_tree, right_tree):
    """
    Выполняет слияние двух АВЛ-деревьев в одно.
    """
    left_avl = in_order(left_tree)
    right_avl = in_order(right_tree)
    merged_avl = sorted(left_avl + right_avl)
    return create_avl(merged_avl)

def count(root):
    """
        Возвращает количество узлов в АВЛ-дереве.
    """
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)

def check_avl(root):
    """
        Проверяет, является ли дерево корректным АВЛ-деревом.
    """
    if root is None:
        return True

    if abs(get_balance(root)) > 1:
        return False

    if root.left and root.left.key >= root.key:
        return False
    if root.right and root.right.key <= root.key:
        return False

    if root.height != 1 + max(get_height(root.left), get_height(root.right)):
        return False

    return check_avl(root.left) and check_avl(root.right)

def visualize(node, indent, last):
    """
        Выполняет визуализацию дерева в консоль.
    """
    if node:
        res = indent
        if last:
            res += "└─ "
            indent += "   "
        else:
            res += "├─ "
            indent += "│  "
        res += str(node.key) + "\n"
        res += visualize(node.right, indent, False)
        res += visualize(node.left, indent, True)
        return res
    return ''