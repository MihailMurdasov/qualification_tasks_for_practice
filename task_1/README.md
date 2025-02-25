
# **Реализация AVL-дерева**

## **Описание**

Этот код представляет собой реализацию АВЛ-дерева и предоставляет его графическую визуализацию.


## **Операции**

-  **Вставка узла** (`insert`)
-  **Удаление узла** (`delete`)
-  **Поиск узла по значению** (`search`)
-  **Разделение дерева по значению** (`split`)
-  **Слияние двух деревьев** (`merge`)
-  **Проверка на соответствие свойствам АВЛ-дерева** (`check_avl`)
-  **Подсчет количества узлов в дереве** (`count`)
-  **Обходы дерева** (`pre_order`,`in_order`,`post_order`)

## **Структура**

- `get_height` - возвращает высоту узла.
- `update_height` - обновляет высоту узла.
- `get_balance` - возвращает баланс-фактор узла.
- `get_min_value_node` - возвращает узел с минимальным значением.
- `get_max_value_node` - возвращает узел с максимальным значением.
- `balance` - выполняет балансировку АВЛ-дерева с помощью поворотов.
- `right_rotate` - выполняет правый поворот узла.
- `left_rotate` - выполняет левый поворот узла.
- `insert` - добавляет новый узел, поддерживая балансировку.
- `delete` - удаляет узел, восстанавливая дерево.
- `delete_max` - удаляет узел с максимальным значением.
- `delete_min` - удаляет узел с минимальным значением.
- `pre_order` - выполняет pre-order обход и возвращает массив элементов.
- `post_order` - выполняет post-order обход и возвращает массив элементов.
- `in_order` - выполняет in-order обход и возвращает массив элементов.
- `search` - выполняет поиск узла по значению.
- `create_avl` - создает АВЛ-дерево по отсортированному массиву элементов.
- `split` - разделяет АВЛ-дерево на два разных по заданному значению.
- `merge` - объединяет два АВЛ-дерева в одно.
- `count` - возвращает количество узлов в дереве.
- `check_avl` - проверяет АВЛ-дерево на соответствие свойствам.
- `vizualize` - выполняет простую текстовую визуализацию.

## **Тестирование**

Для проверки данной реализации доступны тесты в файле `tests.py`. Запустить тесты можно командой:
```
pytest tests.py
```
