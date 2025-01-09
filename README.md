# TODO アプリ: Python & Angular

このリポジトリは、Python (Flask) をバックエンド、Angular をフロントエンドとして使用した TODO アプリの練習プロジェクトです。

## 全体構成

ディレクトリ構成:

```bash
todo-learn-pyng/
├── backend/    # バックエンド用ディレクトリ(Python,Flask)
├── docs/       # 全体ドキュメント              
├── frontend/   # フロントエンド用ディレクトリ(Angular)
├── README.md   # プロジェクト全体の説明
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

ディレクトリ構成:

```bash
backend/                  # バックエンド用ディレクトリ
├── venv/                 # 仮想環境フォルダ (Git管理対象外)
├── app.py                # Flask アプリのエントリーポイント
├── requirements.txt      # Python依存関係
├── instance/             # インスタンスディレクトリ
│   └── todos.db          # SQLite データベース (Git管理対象外)
├── docs/                 # API ドキュメント
│   └── swagger.yaml      # Swagger/OpenAPI ドキュメント
├── tests/                # テスト用ディレクトリ
│   └── test_app.py
└── .gitignore
```

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

ディレクトリ構成:

```bash
frontend/
├── README.md                # フロントエンドの説明
├── angular.json             # Angular CLI 設定
├── node_modules/            # 依存関係（自動生成）
├── package-lock.json        # npm 依存関係ロックファイル
├── package.json             # npm 依存関係
├── public/                  # 静的ファイル（画像など）
├── src/                     # ソースコード
│   ├── app/                 # アプリケーションロジック
│   ├── index.html           # メインのHTMLファイル
│   ├── main.ts              # アプリケーションのエントリーポイント
│   ├── styles.scss          # グローバルスタイル
├── tsconfig.app.json        # アプリ用TypeScript設定
├── tsconfig.json            # TypeScript全般の設定
├── tsconfig.spec.json       # テスト用TypeScript設定
└── .gitignore               # Git無視設定
```

### 環境構築

開発環境

```bash
todo-learn-pyng % node -v
v22.4.1
todo-learn-pyng % npm -v
10.8.1
```

Angular CLI インストール

```bash
# グローバルにインストールされる
% npm install -g @angular/cli

# インストールしたらngコマンドを確認
% which ng
/Users/<user>/.nvm/versions/node/v22.4.1/bin/ng
```

### Angularプロジェクト作成

```bash
ng new frontend
```

オプション

- Autocomplete -> Yes
- share pseudonymous usage data -> No
- Which stylesheet format -> Sass
- SSR or SSG -> No
