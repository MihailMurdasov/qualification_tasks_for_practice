import pytest
from AVLTree import *


def test_insert_root():
    root = insert(None, 5)
    assert root.key == 5  and check_avl(root) is True

def test_insert_left():
    root = insert(None, 5)
    root = insert(root, 3)
    assert root.left.key == 3 and check_avl(root) is True

def test_insert_right():
    root = insert(None, 5)
    root = insert(root, 10)
    assert root.right.key == 10 and check_avl(root) is True

def test_height():
    root = create_avl([10,20,30,40,50,60])
    assert get_height(root) == 3

def test_height_zero():
    root = None
    assert get_height(root) == 0

def test_update_height():
    root = create_avl([10,20,30])
    root = insert(root, 40)
    update_height(root)
    assert root.height == 3

def test_delete():
    root = None
    for i in [10, 20, 30, 40, 50]:
        root = insert(root, i)
    root = delete(root, 30)
    assert in_order(root) == [10,20,40,50] and check_avl(root) is True

def test_delete_none():
    root = None
    root = delete(root, 30)
    assert root is None

def test_delete_root():
    root = create_avl([10,20,30,40,50,60])
    root = delete(root, 40)
    assert root.key == 50 and check_avl(root) is True

def test_delete_min():
    root = create_avl([10,20,30,40,50,60])
    root = delete_min(root)
    assert get_min_value_node(root).key == 20 and check_avl(root) is True

def test_delete_min_none():
    root = None
    root = delete_min(root)
    assert root is None

def test_delete_max():
    root = create_avl([10,20,30,40,50,60])
    root = delete_max(root)
    assert get_max_value_node(root).key == 50 and check_avl(root) is True

def test_delete_max_none():
    root = None
    root = delete_max(root)
    assert root is None

def test_pre_order():
    root = create_avl([1,2,3,4,5])
    assert pre_order(root) == [3,2,1,5,4]

def test_pre_order_none():
    root = None
    assert pre_order(root) == []

def test_in_order():
    root = create_avl([1,2,3,4,5])
    assert in_order(root) == [1,2,3,4,5]

def test_in_order_none():
    root = None
    assert in_order(root) == []

def test_post_order():
    root = create_avl([1,2,3,4,5])
    assert post_order(root) == [1,2,4,5,3]

def test_post_order_none():
    root = None
    assert post_order(root) == []

def test_search_true():
    root = create_avl([10,20,30,40,50,60])
    assert search(root, 20) is True

def test_search_false():
    root = create_avl([10,20,30,40,50,60])
    assert search(root, 999) is False

def test_search_none():
    root = None
    assert search(root, 999) is False

def test_get_min():
    root = create_avl([10,20,30,40,50,60])
    assert get_min_value_node(root).key == 10

def test_get_min_none():
    root = None
    assert get_min_value_node(root) is None

def test_get_max():
    root = create_avl([10,20,30,40,50,60])
    assert get_max_value_node(root).key == 60

def test_get_max_none():
    root = None
    assert get_max_value_node(root) is None

def test_get_balance():
    root = insert(None, 10)
    root = insert(root, 5)
    assert get_balance(root) == 1

def test_get_balance_zero():
    root = None
    assert get_balance(root) == 0

def test_left_rotation():
    root = None
    for i in [10, 20, 30, 40, 50]:
        root = insert(root, i)

    root = insert(root, 60)
    root = insert(root, 80)
    root = insert(root, 100)
    assert root.right.right.key == 80

def test_right_rotation():
    root = None
    for i in [10, 20, 30, 40, 50]:
        root = insert(root, i)

    root = insert(root, 1)
    root = insert(root, 2)
    root = insert(root, 3)
    assert root.left.left.key == 1

def test_split():
    root = create_avl([10,20,30,40,50,60])
    left_tree, right_tree = split(root, 30)
    assert in_order(left_tree) == [10,20] and in_order(right_tree) == [30,40,50,60] and check_avl(left_tree) is True and check_avl(right_tree) is True

def test_split_limit_value():
    root = create_avl([10,20,30,40,50,60])
    left_tree, right_tree = split(root, 10)
    assert in_order(left_tree) == [] and in_order(right_tree) == [10,20,30,40,50,60] and check_avl(left_tree) is True and check_avl(right_tree) is True

def test_split_invalid_key():
    root = create_avl([10,20,30,40,50,60])
    left_tree, right_tree = split(root, 999)
    assert left_tree is None and right_tree is None

def test_create_avl():
    root = create_avl([10,20,30,40])
    assert in_order(root) == [10,20,30,40] and check_avl(root) is True

def test_create_avl_none():
    root = create_avl([])
    assert root is None

def test_create_avl_one_elem():
    root = create_avl([1])
    assert in_order(root) == [1] and check_avl(root) is True and root.key == 1

def test_merge():
    first_tree = create_avl([10,20,30])
    second_tree = create_avl([40,50,60])
    merged_tree = merge(first_tree, second_tree)
    assert in_order(merged_tree) == [10,20,30,40,50,60] and check_avl(merged_tree) is True

def test_merge_one_empty():
    first_tree = create_avl([])
    second_tree = create_avl([40,50,60])
    merged_tree = merge(first_tree, second_tree)
    assert in_order(merged_tree) == [40,50,60] and check_avl(merged_tree) is True

def test_merge_empty():
    first_tree = create_avl([])
    second_tree = create_avl([])
    merged_tree = merge(first_tree, second_tree)
    assert in_order(merged_tree) == [] and check_avl(merged_tree) is True

def test_count():
    root = create_avl([10,20,30,40,50,60])
    assert count(root) == 6

def test_count_zero():
    root = None
    assert count(root) == 0

def test_check_avl():
    root = create_avl([10,20,30,40,50,60])
    assert check_avl(root) is True

def test_check_avl_none():
    root = create_avl([])
    assert check_avl(root) is True

def test_check_avl_invalid_balance():
    root = AVLNode(10)
    root.left = AVLNode(9)
    root.left.left = AVLNode(8)
    root.left.left.left = AVLNode(7)
    assert check_avl(root) is False

def test_check_avl_left_is_bigger_than_right():
    root = AVLNode(10)
    root.left = AVLNode(40)
    root.right = AVLNode(1)
    assert check_avl(root) is False

def test_check_avl_left_is_equal_right():
    root = AVLNode(10)
    root.left = AVLNode(40)
    root.right = AVLNode(40)
    assert check_avl(root) is False

def test_check_avl_invalid_root_height():
    root = AVLNode(10)
    root.left = AVLNode(1)
    root.right = AVLNode(2)
    root.height = 12312
    assert check_avl(root) is False