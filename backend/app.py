from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# SQLiteデータベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# データベースモデルの定義
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {"id": self.id, "task": self.task, "completed": self.completed}


# データベースの初期化
@app.before_request
def initialize_app():
    if not hasattr(app, 'initialized'):
        with app.app_context():
            db.create_all()  # テーブルを作成
            # 初回データ挿入（必要な場合）
            if Todo.query.count() == 0:
                todos = [
                    {"task": "Learn Angular", "completed": False},
                    {"task": "Build TODO App", "completed": False},
                ]
                for todo in todos:
                    db.session.add(
                        Todo(task=todo["task"], completed=todo["completed"])
                        )
                db.session.commit()
        app.initialized = True


# GET: 全てのTODOを取得
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.to_dict() for todo in todos])


# POST: 新しいTODOを追加
@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.json
    new_todo = Todo(task=data["task"], completed=data.get("completed", False))
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201


# UPDATE: TODOを更新
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    print(f"Received data for update: {data}")

    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"message": "Todo not found"}), 404
    todo.task = data.get('task', todo.task)
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify(todo.to_dict()), 200


# DELETE: TODOを削除
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"message": "Todo deleted"}), 200
    else:
        return jsonify({"error": "Todo not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
