from HashTable import *


def main():
    table = HashTable()

    print("Добавление элементов: 1:banana, 2:apple, 3:moevm")
    table.put("1", "banana")
    table.put("2", "apple")
    table.put("3", "moevm")

    print("\nget(1): ", table.get("1"))
    print("get(2): ", table.get("2"))
    print("get(3): ",table.get("3"))

    print("\nКлюч 1 есть в таблице: ","1" in table)
    print("Ключ 4 есть в таблице: ","4" in table)

    print("\nУдаление элемента по ключу 2")
    table.remove("2")
    print("Ключ 2 есть в таблице: ","2" in table)

    print("\nКоличество элементов: ",len(table))

    print("\nДобавление элемента 4:aisd")
    table["4"] = "aisd"
    value = table["4"]
    print(table["4"], value)

    print("\nУдаление элемента по ключу 4")
    del table["4"]
    print("Ключ 4 есть в таблице: ","4" in table)

    print("\nkeys(): ",table.get_keys())
    print("values(): ",table.get_values())
    print("items(): ",table.get_items())

if __name__ == "__main__":
    main()