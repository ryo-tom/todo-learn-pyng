# TODO アプリ: Python & Angular

このリポジトリは、Python (Flask) をバックエンド、Angular をフロントエンドとして使用した TODO アプリの練習プロジェクトです。

## 全体構成

完成イメージ:

```bash
todo-learn-pyng/
├── backend/                  # バックエンド用ディレクトリ
│   ├── venv/                 # 仮想環境フォルダ
│   ├── app.py                # Flask アプリのエントリーポイント
│   ├── requirements.txt      # Python依存関係
│   ├── docs/                 # API ドキュメント
│   │   └── swagger.yaml      # Swagger/OpenAPI ドキュメント
│   ├── tests/                # テスト用ディレクトリ
│   │   └── test_app.py
│   └── .gitignore
├── frontend/                 # フロントエンド用ディレクトリ
│   ├── src/                  # Angular のソースコード
│   ├── angular.json          # Angular CLI 設定
│   └── .gitignore
├── README.md                 # プロジェクト全体の説明
└── .gitignore
```

## 開発環境

バックエンド:

- **Python**: バージョン 3.12 以上
- 主要ライブラリ:
  - Flask
  - Flask-CORS
  - Flask-SQLAlchemy

フロントエンド:

- **Node.js**: バージョン 22.4 以上
- **Angular CLI**: 最新バージョン

ツール:

- Swagger Viewer (VSCode 拡張機能) [[ref]](https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer)

## バックエンドセットアップ: Python (Flask)

### 新規プロジェクトのセットアップ

#### 仮想環境の作成と有効化

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境を有効化
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

#### 必要なライブラリのインストール

```bash
pip install flask flask-cors
```

#### 依存関係を記録

仮想環境内でインストールされたライブラリを `requirements.txt` に保存します。

```bash
pip freeze > requirements.txt
```

### 既存プロジェクトのセットアップ

#### 依存関係のインストール

```bash
pip install -r requirements.txt
```

### サーバーの起動

```bash
python app.py
```

<http://127.0.0.1:5000> にアクセス。

### API確認テスト

サーバーを起動したらAPIを確認

todo取得:

```bash
curl -X GET http://127.0.0.1:5000/api/todos
```

新規登録:

```bash
curl -X POST http://127.0.0.1:5000/api/todos \
-H "Content-Type: application/json" \
-d '{"task": "Write Docs", "completed": false}'
```

削除:

```bash
curl -X DELETE http://127.0.0.1:5000/api/todos/4
```

## フロントエンドセットアップ: Angular

WIP:
