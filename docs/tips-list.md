# Python: List で特定レコードを削除する方法

## 概要

Python でリストから特定のレコードを削除するには、不要なレコードを検索してから削除する必要があります。ここでは、特定の `id` に一致したレコードをリストから削除するための効率的な方法を述べます。

## 方法 1: **`remove` を使用**

リスト内の一致する要素を指定して削除します。

コード

```python
todos = [
    {"id": 1, "task": "Learn Angular", "completed": False},
    {"id": 2, "task": "Build TODO App", "completed": False},
    {"id": 3, "task": "Test API", "completed": True},
]

todo_id = 2

# 該当するTODOを削除
for todo in todos:
    if todo["id"] == todo_id:
        todos.remove(todo)
        break  # 一致するレコードは1つだけと仮定
```

解説

- **`remove` メソッド** は、リストから指定した要素を削除します。
- 一致する要素が要素ごとに表現されている場合に適しています。


## 方法 2: **インデックスで削除**
インデックスを持って要素を別の方法で削除します。

コード

```python
todos = [
    {"id": 1, "task": "Learn Angular", "completed": False},
    {"id": 2, "task": "Build TODO App", "completed": False},
    {"id": 3, "task": "Test API", "completed": True},
]

todo_id = 2

# 該当するTODOを削除
for i, todo in enumerate(todos):
    if todo["id"] == todo_id:
        del todos[i]
        break
```

解説

- **`enumerate`** で要素とそのインデックスを取得します。
- **`del`** を使うことで、リスト内の指定された要素を削除します。
- 直接インデックスで操作するので、リストのサイズが大きい場合に保存コストが低くなります。



## 方法 3: **`next` を使用**

新しいリストを作ることなく、直接該当要素を指定して削除します。

コード

```python
todos = [
    {"id": 1, "task": "Learn Angular", "completed": False},
    {"id": 2, "task": "Build TODO App", "completed": False},
    {"id": 3, "task": "Test API", "completed": True},
]

todo_id = 2

# 一致するTODOを取得
todo_to_remove = next((todo for todo in todos if todo["id"] == todo_id), None)

if todo_to_remove:
    todos.remove(todo_to_remove)
```

解説

- **`next` 関数**
  - 条件に一致する最初の要素を取得します。
  - 1要素しか要らないので、効率が良いです。
- 要素が見つからない場合には `None` を返すので、エラーを作りません。

---

## 比較表

| 方法           | メリット                                   | デメリット                           |
|----------------|-------------------------------------------|--------------------------------------|
| **`remove`**    | シンプルで直感的                         | リストに一致する要素が必要           |
| **インデックス** | インデックスを指定できるため极めて強力 | リストが大きいとコストが上昇         |
| **`next`**      | 簡潔で高効率                             | 条件に一致する要素が要求される。 |


