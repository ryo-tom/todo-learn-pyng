# Pythonの基礎

```py
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
```

```python
[<expression> for <item> in <iterable> if <condition>]
```

この文法は、**リスト内包表記(List Comprehensions)**と呼び、既存のリストから新しいリストを作ることができる、リスト作成方法の一つ。

- **`<expression>`**
  - 生成されるリストの各要素を定義します。
  - `<expression>` は `<item>` を使った任意の式を書くことができます（そのまま使ったり、計算や変換をしたり）。
- **`for <item> in <iterable>`**
  - `<iterable>` の各要素を `<item>` に順番に取り出します。
- **`if <condition>`** _(省略可能)_
  - 条件を満たす場合のみ、リストに含めます。

## リスと内包表記の具体例

`<expression>`をそのまま使う例:

```python
evens = [x for x in range(10) if x % 2 == 0]
```

- **`for x in range(10)`**: `x` が 0, 1, 2, ..., 9 を順番に取り出します。
- **`if x % 2 == 0`**: 偶数の場合のみ `<expression>` を実行。
- **`<expression>`**: `x` をそのままリストに追加。

`<expression>`を計算して使う例:

```python
squares = [x * x for x in range(5)]
```

- **`for x in range(5)`**: `x` が 0, 1, 2, 3, 4 を順番に取り出します。
- **`<expression>`**: `x * x` が計算され、新しいリストの要素として使われます。

結果は、`squares = [0, 1, 4, 9, 16]`

## todoを削除する他の方法

### 方法 1: リストのメソッド remove を使用する

Pythonのリストには、指定した要素を削除するための remove メソッドがあります。

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
        break  # 一致するレコードは1つだけと仮定して終了
```