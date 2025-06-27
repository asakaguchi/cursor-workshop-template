# Cursor×Python×GitHub ハンズオン

## AI と一緒にプログラミングを始めよう！🚀

### 🎯 今日のゴール

プログラミング未経験でも大丈夫！今日は以下のことができるようになります。

1. **AI ペアプログラミング**：Cursor を使って AI と対話しながらコードを書く
2. **プロジェクト管理**：GitHub でタスクを管理し、コードを共有する
3. **品質の高いコード**：テストを書きながら安心して開発を進める
4. **動くアプリ完成**：シンプルな商品管理 API を作り上げる

難しそうに聞こえるかもしれませんが、AI がずっと隣にいてサポートしてくれます。一緒に楽しく学びましょう！

---

## 📋 タイムスケジュール（2 時間）

| 時間 | 内容 | ポイント |
|------|------|----------|
| 0:00-0:25 | 環境構築とセットアップ | 開発の準備を整えよう |
| 0:25-0:40 | Human-in-the-Loop 開発の体験 | AI との対話方法を学ぼう |
| 0:40-1:10 | Issue 駆動開発の実践 | タスクを分解して進めよう |
| 1:10-1:45 | TDD で API 開発 | テストを書きながら開発しよう |
| 1:45-2:00 | 完成とまとめ | 動くアプリを確認しよう |

---

## 🛠️ Part 1：環境構築（25 分）

開発を始める前に、必要なツールをインストールしましょう。コピー＆ペーストで進められるので安心してください。

**📝 対象 OS**：このワークショップは macOS を対象としています。

**🐳 開発環境**：このワークショップでは Docker を使用します。

- 環境差異がなく、確実に動作
- 依存関係の問題が起こらない
- VS Code Dev Container で快適な開発体験

### 1.1 Cursor のインストール

#### インストール手順

1. **ダウンロード**
   - [cursor.com](https://cursor.com) にアクセス
   - 「ダウンロード MacOS」ボタンをクリック
   - ファイル名やダウンロード先を確認（必要に応じて変更）して「保存」ボタンをクリック

1. **インストール実行**
   - ダウンロードしたファイルを開く
   - Cursor アイコンを Application アイコンにドラッグ＆ドロップ

1. **Cursor の起動**
   - Launchpad から Cursor を起動

#### 初期設定

初回起動時に以下の設定を行います。

1. **ログイン方法の選択**
   - **GitHub アカウントで**サインイン
1. **エディター設定**
   - テーマのカスタマイズ
   - キーバインドの設定
   - データ共有事項についての内容を確認し、チェックボックスをオンにし、「Continue」ボタンをクリック
     （デフォルトでは、データが学習に使われる設定になっているので、学習されないように後で設定を変更する）
   - 言語設定とターミナルコマンドの設定
     - Language for AI → Japanese
     - Open from Terminal → `cursor` command → 「Install」ボタンをクリック
     - 「Continue」ボタンをクリック
1. **プライバシー設定**
   - 右上の歯車アイコンをクリック
   - 「General」→「Privacy」→「Privacy Mode with Storage」に変更
1. **Japanese Language Pack 拡張機能のインストール**
   - 拡張機能を開く（`Cmd`+`Shift`+`X`）
   - 入力欄に、`Japanese` と入力
   - `Japanese Language Pack for Visual Studio Code` 拡張機能の `Install` ボタンをクリック
   - 画面左下に、`Would you like to change Cursor's display language to Japanese and restart?` とメッセージが表示されたら、そこに表示されている `Change Language and Restart` ボタンをクリック

**💡 ポイント**：

- Cursor Pro の 14 日間無料トライアル付き
- 初期設定は後から変更可能
- VS Code の設定や拡張機能も移行可能

### 1.2 Docker Desktop のインストール

1. [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/) にアクセス
1. 「Download Docker Desktop」にマウスカーソルを合わせる
   - Apple Silicon Mac（M1/M2/M3）：「Download for Mac - Apple Silicon」をクリック
   - Intel Mac：「Download for Mac - Intel Chip」をクリック
1. ファイル名やダウンロード先を確認（必要に応じて変更）して「保存」ボタンをクリック
1. ダウンロードしたファイルを開く
1. Docker アイコンを Application アイコンにドラッグ＆ドロップ
1. Launchpad から Docker を起動
1. Docker Subscription Service Agreement の画面で、「Accept」ボタンをクリック
1. 「Use recommended settings (requires password)」を選択し、「Finish」ボタンをクリック
   - macOS アカウントのパスワードを入力
1. Welcome to Docker の画面で、「Skip」リンクをクリック
1. Welcome Survey の画面で、「Skip」リンクをクリック

**動作確認**：

```bash
# Docker が正しくインストールされたか確認
docker --version
docker compose version
```

### 1.3 プロジェクトの準備

テンプレートリポジトリから自分のプロジェクトを作成します。

```bash
# ブラウザでテンプレートリポジトリを開く
open https://github.com/asakaguchi/cursor-workshop-template
```

または、ブラウザで直接 <https://github.com/asakaguchi/cursor-workshop-template> にアクセスしてください。

GitHub ページで以下の手順を実行します。

1. **「Use this template」ボタンをクリック**（緑色のボタン）
1. **「Create a new repository」を選択**
1. **Repository name**：`my-cursor-workshop`（またはお好きな名前）
1. **「Create repository」をクリック**

**⚠️ 注意**：リポジトリの作成には数秒かかる場合があります。

次に、作成したリポジトリをローカルにクローンし、Cursor で開きます。

**💡 ベストプラクティス**：開発プロジェクトは `~/Projects` ディレクトリで管理することを推奨します。デスクトップではなく専用ディレクトリを使うことで、プロジェクトの整理と管理が容易になります。

```bash
# 開発用ディレクトリを作成・移動
mkdir -p ~/Projects
cd ~/Projects

# 自分のリポジトリをクローン（YOUR_USERNAME は自分の GitHub ユーザー名）
git clone https://github.com/YOUR_USERNAME/my-cursor-workshop.git
cd my-cursor-workshop

# Cursor で開く
cursor .
```

### 1.4 Dev Container で開く

1. Cursor でプロジェクトを開くと、「Dev Containers」拡張機能のインストールを推奨するポップアップが表示されます
   - 「Install」ボタンをクリックしてインストール
1. コマンドパレットを開く（`Cmd`+`Shift`+`P`）
1. 「`Dev Containers: Reopen in Container`」と入力して選択
   一部入力すると候補が表示されるので、候補の中に「`Dev Containers: Reopen in Container`」が表示されたらそれをクリック
1. 初回は Docker イメージのビルドに数分かかります
   ネットワーク環境やマシンスペックにより 5-15 分程度かかる場合があります。
   コーヒーでも飲みながら待ちましょう ☕
1. 完了すると、ターミナルが表示されます

### 1.5 GitHub CLI の認証設定

開発の準備として、GitHub CLI の認証を済ませておきます。

開いているターミナルで、以下のコマンドを入力します。

```bash
gh auth login
```

認証プロンプトが表示されたら、以下の手順で認証を進めます。

1. **What account do you want to log into?** → `GitHub.com` を選択し、`ENTER` キーを押す
1. **What is your preferred protocol for Git operations?** → `HTTPS` を選択し、`ENTER` キーを押す
1. **Authenticate Git with your GitHub credentials?** → `ENTER` キーを押す
1. **How would you like to authenticate GitHub CLI?** → `Login with a web browser` を選択し、`ENTER` キーを押す
1. **Press Enter to open github.com in your browser...** → `Enter` キーを押す
1. ブラウザが開くので、表示されたワンタイムコードを入力
1. GitHub にログインして認証を完了

**💡 ポイント**：

- 認証は **Part 3（Issue 駆動開発）の前まで** に完了すれば OK
- 基本的な `git` コマンド（add、commit 等）は認証なしでも動作
- GitHub CLI 機能（Issue 作成、PR 作成等）には認証が必要

**💡 Dev Container の利点**：

- Python、uv、必要なツールがすべてインストール済み
- Cursor の拡張機能も自動でインストール
- チーム全員が同じ環境で開発可能

**💡 ポイント**：テンプレートリポジトリを使うことで、必要なファイルがすべて揃った状態から始められます。Dev Container を使用することで、Python とすべての開発ツールが自動的にセットアップされます。

🎉 **できたこと**：

- ✅ 開発環境の構築が完了
- ✅ AI と一緒に開発する準備が整った

---

## 🤝 Part 2：Human-in-the-Loop 開発を体験（15 分）

### 2.1 Cursor の AI 機能を理解しよう

Cursor には主に 3 つの AI 機能があります。

1. **チャット（Cmd+L）**：AI と対話しながら開発
1. **インライン編集（Cmd+K）**：コードを直接編集
1. **Composer（Cmd+I）**：複数ファイルの同時編集

今日は主に**チャット機能**を使います。

### 2.2 最初の AI との対話

画面右側のチャットパネルに以下のメッセージを入力してみましょう。

```text
@requirements.md を読んで、どんなアプリを作るのか教えてください。
初心者にもわかりやすく説明してください。
```

AI が要件を説明してくれます。わからない用語があれば、続けて質問してみましょう。

```text
API って何ですか？もっと簡単に説明してください。
```

### 2.3 Cursor Rulesの確認

プロジェクトには「Cursor Rules」という開発ルールが設定されています。

```text
.cursor/rules/ にあるファイルを見て、このプロジェクトの開発ルールを
箇条書きでまとめてください。
```

**💡 ポイント**：

- AI は常にこれらのルールに従って回答してくれます
- このプロジェクトはモダンな **src レイアウト**を採用しています（コードは `src/product_api/` に配置）

これらのルールにより、AI は常に：

- 一貫したコーディングスタイルを維持
- ベストプラクティスに従った実装
- プロジェクト固有の規約を遵守

してくれます。

---

## 📝 Part 3：Issue 駆動開発の実践（30 分）

### 3.1 タスクの分解を依頼

大きなタスクを小さく分解することで、開発が進めやすくなります。AI に以下を依頼してみましょう。

```text
@requirements.md @.cursor/prompts/task-breakdown.md

要件を確認して、2 時間で完成できるようにタスクを分解してください。
各タスクは 15-30 分で完了できる粒度にしてください。
```

**💡 ポイント**: `@.cursor/prompts/task-breakdown.md` ファイルは、タスク分解の具体的なガイドラインを提供します。このファイルを参照することで、AI がより適切にタスクを分解してくれます。

AI がタスクの一覧を提示してくれます。

### 3.2 GitHub Issue の作成

タスクの内容を確認して問題なければ、シンプルに返答しましょう。

```text
ok
```

と入力するだけで、AI が自動的に GitHub Issue を作成してくれます。

### 3.3 Issue の確認

ブラウザで以下を確認：

```bash
gh repo view --web
```

「Issues」タブを見ると、作成されたタスクが一覧で見えます。

**💡 ポイント**：各 Issue には番号（#1、#2 など）が付いており、これがタスクの識別子になります。

🎉 **できたこと**：

- ✅ タスクの分解と可視化が完了
- ✅ GitHub でプロジェクト管理の準備が整った

---

## 🧪 Part 4：TDD で API 開発（30 分）

**📝 Dev Container 使用時の注意**: 以降のコマンドは Dev Container 内で実行されるため、`docker compose exec app` を省略して直接コマンドを実行できます。Dev Container のターミナルは、すでにコンテナ内部で動作しています。

### 4.1 最初のタスク開始

AI に最初のタスクを始めることを伝えます。

```text
Task 1 を開始してください
```

AI が以下の作業を自動で進めます。

1. 新しいブランチを作成
1. 必要なファイルを作成（`src/product_api/` 配下に配置）
1. テストを先に書く（TDD）

### 4.2 TDD のサイクルを体験

TDD（テスト駆動開発）は以下の 3 ステップで進めます。

1. **Red**：失敗するテストを書く
1. **Green**：テストを通す最小限のコード
1. **Refactor**：コードを改善

AI がこのサイクルを実践しながら開発を進めます。

### 4.3 テストの実行

Dev Container 内では以下のコマンドを直接実行できます：

```bash
# テストを実行（カバレッジ付き）
uv run pytest

# 詳細出力でテスト実行
uv run pytest -v

# 特定のテストだけ実行
uv run pytest tests/test_specific.py -v
```

**💡 ポイント**: Dev Container 環境では、すでにコンテナ内にいるため `docker compose exec app` は不要です。

**💡 ポイント**：最初は赤い文字（テスト失敗）が表示され、実装を進めると緑（テスト成功）に変わります。

### 4.4 プルリクエストの作成

**✅ タスク完了の目安**：

- すべてのテストが緑色（成功）になった
- コードが期待通りに動作している
- リファクタリングが必要なら完了している

タスクが完了したら、AI に伝えましょう。

```text
Task 1 が完了しました。PR を作成してください。
```

AI が以下の作業を自動で進めます。

1. コードをコミット
1. GitHub にプッシュ
1. プルリクエストを作成

🎉 **できたこと**：

- ✅ TDD で品質の高いコードを実装
- ✅ GitHub でコードレビューの準備が完了

---

## 🎉 Part 5：完成とまとめ（15 分）

### 5.1 API の動作確認

全てのタスクが完了したら、実際に API を動かしてみましょう。

Dev Container 内で実行：

```bash
# API サーバーを起動
uvicorn src.product_api.main:app --reload --host 0.0.0.0 --port 8000
```

別のターミナルタブを開いて（Cursor のターミナルで `+` ボタンをクリック）：

```bash
# 商品を作成
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "テスト商品", "price": 1000}'

# 作成した商品を取得
curl -X GET "http://localhost:8000/items/1"
```

### 5.2 Swagger UI での確認

ブラウザで <http://localhost:8000/docs> にアクセスすると、API の仕様が視覚的に確認できます。

### 5.3 学んだことの振り返り

今日体験したことをまとめましょう。

✅ **Human-in-the-Loop 開発**

- AI と対話しながら開発
- 人間が方向性を決め、AI が実装

✅ **Issue 駆動開発**

- タスクを小さく分解
- 進捗が見える化

✅ **TDD（テスト駆動開発）**

- バグの少ないコード
- 安心して修正できる

✅ **実践的な開発フロー**

- Git/GitHub でバージョン管理
- プルリクエストでコードレビュー

---

## 🚀 次のステップ

### さらに学ぶには

1. **機能追加に挑戦**
   - 商品の更新（PUT）
   - 商品の削除（DELETE）
   - 商品一覧の取得（GET /items）

1. **データベース連携**
   - SQLite を使った永続化
   - SQLAlchemy の導入

1. **認証機能の追加**
   - JWT トークン認証
   - ユーザー管理

### 役立つリソース

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)
- [Cursor公式ドキュメント](https://docs.cursor.com/)
- [GitHub Skills](https://skills.github.com/)

---

## 💡 トラブルシューティング

**💡 エラーは学習のチャンス**：
プログラミングではエラーは日常茶飯事です。エラーメッセージは「何が問題か」を教えてくれる大切な情報です。焦らず、以下の解決法を試してみましょう。

### よくある問題と解決法

#### Q：コメント行でエラーが出る

```text
zsh: command not found: #
```

**解決法**: コメント行（`#` で始まる行）は実行しないでください。コードブロック内のコマンドのみ実行してください。

#### Q：「brew install sh」でエラーが出る

```text
Warning: No available formula with the name "sh". Did you mean shc?
```

**解決法**: 正しくは `brew install gh` です。`sh` ではなく `gh` (GitHub CLI) をインストールしてください。

#### Q：警告メッセージが表示される

```text
WARN: The following commands are shadowed by other commands in your PATH: uv uvx
```

**解決法**: 既存のツールがあることを示す警告です。問題ありません。そのまま続行してください。

#### Q：GitHub CLI の更新通知が表示される

```text
A new release of gh is available: 2.74.0 → 2.74.1
To upgrade, run: brew upgrade gh
```

**解決法**: 更新は任意です。ハンズオン中は無視して構いません。後で `brew upgrade gh` で更新できます。

### Docker 関連のトラブルシューティング

#### Q：Docker Desktop が起動していない

```text
Cannot connect to the Docker daemon at unix:///var/run/docker.sock.
```

**解決法**: Docker Desktop アプリケーションを起動してください。
メニューバーに Docker アイコンが表示されます。

#### Q：Docker コンテナのポートが使用中

```text
bind: address already in use
```

**解決法**:

```bash
# 使用中のコンテナを停止
docker compose down

# または別のポートを使用
# compose.yml を編集して "8000:8000" を "8001:8000" に変更
```

#### Q：Cursor で "Reopen in Container" が表示されない

**解決法**:

1. Cursor に Dev Containers 拡張機能をインストール
1. 拡張機能を検索："ms-vscode-remote.remote-containers"
1. インストール後、Cursor を再起動

#### Q：Cursor Pyright 設定のインポートについて

Dev Container 起動時に「Would you like Cursor Pyright to import your settings from Pylance?」というダイアログが表示される場合があります。

**推奨回答**：**「No」を選択**

**理由**：

- このプロジェクトには既に最適化された Pyright 設定が `pyproject.toml` で定義済み
- Pylance からの設定をインポートすると、プロジェクト固有の設定が上書きされる可能性がある
- プロジェクトの一貫性を保ち、トラブルシューティングを簡素化するため

**追加推奨**：「Never ask again」もチェックして、今後同様のダイアログを非表示にすることを推奨します。

#### Q：Docker コンテナ内でコマンドが実行できない

**Dev Container を使用している場合**：
ターミナルはすでにコンテナ内で動作しているため、直接コマンドを実行できます：

```bash
# Dev Container のターミナルで直接実行
uv run pytest
```

**Dev Container を使用していない場合**：

```bash
# コンテナに入る
docker compose exec app bash

# または直接コマンドを実行
docker compose exec app uv run pytest
```

#### Q：Docker イメージのビルドが遅い

**解決法**:

- 初回ビルドは時間がかかります（約 5-10 分）
- 2 回目以降はキャッシュが利用されるため高速化されます
- Docker Desktop の設定でメモリを増やすことで改善する場合があります

---

## 🎓 おめでとうございます

2 時間でプログラミングの基礎から API の完成まで体験できました。これはプロの開発者が日々行っている実際のワークフローです。

最も重要なのは、**完璧を求めずに AI と協力しながら前進すること**です。わからないことがあれば、遠慮なく AI に質問してください。

Happy Coding! 🎉
