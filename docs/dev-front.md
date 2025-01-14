# フロントエンド開発メモ

Bootstrap のインストール

```bash
npm install bootstrap
```

angular.json を開き、styles 配列に以下を追加

```json
"styles": [
  "src/styles.scss",
  "node_modules/bootstrap/dist/css/bootstrap.min.css"
]
```

開発サーバーを再起動して Bootstrap を反映

## コンポーネントの作成

1. 必要なコンポーネントを生成する。

   ```bash
   ng generate component components/TodoList
   ng generate component components/TodoItem
   ```

2. 例えば`TodoList`の場合、以下のようなファイルが生成される。

   ```bash
   src/app/components/todo-list/
   ├── todo-list.component.ts       # コンポーネントのロジック
   ├── todo-list.component.html     # コンポーネントのテンプレート
   ├── todo-list.component.scss     # コンポーネントのスタイル
   └── todo-list.component.spec.ts  # コンポーネントのテスト
   ```

---

## サービスの作成

1. `TodoService` を生成する。

   ```bash
   ng generate service services/Todo
   ```

2. 以下のようなファイルが生成される。

   ```bash
   src/app/services/
   ├── todo.service.ts        # サービスの実装ファイル
   └── todo.service.spec.ts   # サービスのテストファイル
   ```

3. 生成した `todo.service.ts` に、以下の機能を実装する。
   - TODO リストを取得する (`GET` リクエスト)。
   - 新しい TODO を追加する (`POST` リクエスト)。
   - TODO を削除する (`DELETE` リクエスト)。

4. `app.config.ts` に `HttpClientModule` を提供する設定を追加する。
   - `provideHttpClient()` を `providers` 配列に登録する。

## 疎通確認

1. 簡易的な疎通確認用ロジックを追加
   - `AppComponent` に `TodoService` をインポートし、TODO リストを取得するロジックを記述。
   - 取得したデータをコンソールログに出力。

2. TODO リストを表示するテンプレートを作成
   - `AppComponent` のテンプレート (`app.component.html`) にリスト表示のコードを記述。

3. `ngFor` ディレクティブを利用するための設定
   - `CommonModule` をインポートし、`AppComponent` の `imports` 配列に登録する。

4. 開発サーバーを起動して確認

   ```bash
   ng serve
   ```

   - ブラウザで <http://localhost:4200> を開き、TODO リストが表示されるか確認。

## エラーが発生した場合

1. `ngFor` エラーが発生した場合:
   - `CommonModule` をインポートして設定する。

2. バックエンドとの通信エラー:
   - Flask サーバーが起動しているか確認する。
   - `TodoService` の `apiUrl` が正しいか確認する。


# TODO アプリ フロントエンド手順書 - ステップ 4

## TODO リストのロジックと UI 実装

### 目的
- バックエンドから取得した TODO リストを操作するロジックを追加。
- 新しい TODO の追加フォームと削除ボタンを UI に実装する。

## 手順

### 1. `TodoList` コンポーネントにロジックを追加
- **バックエンドから TODO を取得**:
  - `TodoService` をインポートし、`ngOnInit` 内で `getTodos` を呼び出してリストを取得する。

- **TODO を削除するロジック**:
  - `TodoService` の `deleteTodo` を呼び出し、削除処理を実装する。
  - 削除成功後、ローカルリストを更新。

### 2. `TodoItem` コンポーネントを更新
- `@Input()` デコレータを使用して、親コンポーネントから TODO データを受け取れるようにする。
- 削除ボタンを追加し、クリック時に削除イベントを発火させる。

### 3. 新しい TODO を追加するフォームを作成
- `TodoList` コンポーネント内にフォームを作成し、入力されたデータを送信するロジックを実装。
- `TodoService` の `addTodo` を呼び出し、追加処理を行う。
- 追加成功後、ローカルリストを更新。

### 4. UI の更新
- Bootstrap のスタイルを活用し、フォームやボタンを装飾。
- TODO リストをリストグループ形式で表示。

---

## 開発サーバーで確認

1. 開発サーバーを起動。
   ```bash
   ng serve
   ```
2. ブラウザで `http://localhost:4200` を開き、以下を確認。
   - TODO リストが表示される。
   - 新しい TODO を追加できる。
   - TODO を削除できる。

---

## エラーが発生した場合

1. **フォームの送信でエラー**:
   - `addTodo` の API URL またはバックエンドの設定を確認する。

2. **削除操作でエラー**:
   - `deleteTodo` のパスが正しいか確認。

---

これでステップ 4 が完了しました。次に進む準備ができたらお知らせください！
