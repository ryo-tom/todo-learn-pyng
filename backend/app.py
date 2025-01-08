from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 仮のTODOリストデータ
todos = [
    {"id": 1, "task": "Learn Angular", "completed": False},
    {"id": 2, "task": "Build TODO App", "completed": False},
]


# GET: 全てのTODOを取得
@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


# POST: 新しいTODOを追加
@app.route('/api/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    todos.append(new_todo)
    return jsonify(new_todo), 201


# DELETE: TODOを削除
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return jsonify({"message": "Todo deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
