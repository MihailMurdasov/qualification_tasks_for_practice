import pytest
from HashTable import *


def test_hash():
    ht = HashTable()
    assert ht._hash("1234") <= 8

def test_quadratic_probe():
    ht = HashTable()
    assert ht._quadratic_probe(123, 4) <= 8

def test_put():
    ht = HashTable()
    ht.put("1", "put")
    assert "1" in ht and ht.get("1") == "put"

def test_get():
    ht = HashTable()
    ht.put("1", "get")
    assert ht.get("1") == "get"

def test_remove():
    ht = HashTable()
    ht.put("1", "remove")
    ht.remove("1")
    assert "1" not in ht

def test_set_item():
    ht = HashTable()
    ht["1"] = "set"
    assert "1" in ht and ht.get("1") == "set"

def test_get_item():
    ht = HashTable()
    ht["1"] = "set"
    temp = ht["1"]
    assert temp == "set"

def test_del_item():
    ht = HashTable()
    ht["1"] = "set"
    del ht["1"]
    assert "1" not in ht

def test_len():
    ht = HashTable()
    ht["1"] = "one"
    ht["2"] = "two"
    ht["3"] = "three"
    assert len(ht) == 3

def test_keys():
    ht = HashTable()
    ht["1"] = "one"
    ht["2"] = "two"
    ht["3"] = "three"
    assert "1" in ht.get_keys() and "2" in ht.get_keys() and "3" in ht.get_keys() and len(ht.get_keys()) == 3

def test_values():
    ht = HashTable()
    ht["1"] = "one"
    ht["2"] = "two"
    ht["3"] = "three"
    assert "one" in ht.get_values() and "two" in ht.get_values() and "three" in ht.get_values() and len(ht.get_values()) == 3

def test_items():
    ht = HashTable()
    ht["1"] = "one"
    ht["2"] = "two"
    ht["3"] = "three"
    assert ("1", "one") in ht.get_items() and ("2", "two") in ht.get_items() and ("3", "three") in ht.get_items() and len(ht.get_items()) == 3

def test_collision_resolution():
    ht = HashTable(capacity=3)
    ht.put("key1", "value1")
    ht.put("key2", "value2")

    assert "key1" in ht and "key2" in ht and ht.get("key1") == "value1" and ht.get("key2") == "value2"

def test_rehashing():
    ht = HashTable(capacity=4, load_factor=0.5)

    ht.put("key1", "value1")
    ht.put("key2", "value2")
    ht.put("key3", "value3")

    assert "key1" in ht and "key2" in ht and "key3" in ht and ht.get("key1") == "value1" and ht.get("key2") == "value2" and ht.get("key3") == "value3" and len(ht) == 3 and ht.capacity == 8