import time
import random
from AVLTree import *
from Vizualize import visualize_avl


def main():
    def generate_array(n, type="increasing"):
        arr = [x for x in range(n)]
        if type == "random":
            random.shuffle(arr)
            return arr
        elif type == "increasing":
            return arr
        elif type == "decreasing":
            arr = arr[::-1]
            return arr

    sizes = [100, 1000, 10000]

    for type in ["random", "increasing", "decreasing"]:
        for size in sizes:
            keys = generate_array(size, type)

            root = None

            start_insert = time.time()
            for key in keys:
                root = insert(root, key)
            end_insert = time.time()

            start_delete_max = time.time()
            root = delete_max(root)
            end_delete_max = time.time()

            start_delete_min = time.time()
            root = delete_min(root)
            end_delete_min = time.time()

            start_delete_all = time.time()
            while root is not None:
                root = delete_min(root)
            end_delete_all = time.time()

            print("=" * 40)
            print(f"[ Объем данных: {size} ({type})]")
            print(f"[ insert ]:")
            print(f"    Время выполнения: {(end_insert - start_insert):.6f} seconds")
            print(f"[ delete_max ]:")
            print(f"    Время выполнения: {(end_delete_max - start_delete_max):.6f} seconds")
            print(f"[ delete_min ]:")
            print(f"    Время выполнения: {(end_delete_min - start_delete_min):.6f} seconds")
            print(f"[ delete_all ]:")
            print(f"    Время выполнения: {(end_delete_all - start_delete_all):.6f} seconds")

    print("=" * 40 + "\n")
    print("Пример визуализации:")
    root = None
    keys = []
    for i in range(30):
        keys.append(i)
    for key in keys:
        root = insert(root, key)

    print(visualize(root, "", True))
    print("Является AVL-деревом: ", check_avl(root))
    print("Минимальное значение: ", get_min_value_node(root).key)
    print("Максимальное значение: ", get_max_value_node(root).key)
    print("In-order обход: ", in_order(root))
    print("Поиск числа 7: ", search(root, 7))
    print("Поиск числа 999: ", search(root, 999))
    split_key = 10
    print("split по значению: ", split_key)
    first, second = split(root, split_key)
    merged_tree = merge(first,second)
    print("In-order дерева first: ", in_order(first))
    print("In-order дерева second: ", in_order(second))
    print("In-order дерева merged_tree: ", in_order(merged_tree))
    print("После split и merge дерево осталось прежним: ", in_order(root) == in_order(merged_tree))
    print(f"Являются АВЛ-деревьями: root={check_avl(root)}, first={check_avl(first)}, second={check_avl(second)}, merged_tree={check_avl(merged_tree)}")
    print(f"Количество элементов до split и merge: {count(root)}, Количество элементов после split и merge: {count(first)} + {count(second)} = {count(merged_tree)} -> {count(first) + count(second) == count(merged_tree)}")
    visualize_avl(root, "avl_root")
    visualize_avl(first, "avl_first")
    visualize_avl(second, "avl_second")
    visualize_avl(merged_tree, "avl_merged_tree")

if __name__ == "__main__":
    main()
