# Cursor×Python×GitHub ハンズオン

## AIと一緒にプログラミングを始めよう！🚀

### 🎯 今日のゴール

プログラミング未経験でも大丈夫！今日は以下のことができるようになります：

1. **AIペアプログラミング**：Cursor を使って AI と対話しながらコードを書く
2. **プロジェクト管理**：GitHub でタスクを管理し、コードを共有する
3. **品質の高いコード**：テストを書きながら安心して開発を進める
4. **動くアプリ完成**：シンプルな商品管理 API を作り上げる

難しそうに聞こえるかもしれませんが、AI がずっと隣にいてサポートしてくれます。一緒に楽しく学びましょう！

---

## 📋 タイムスケジュール（2時間）

| 時間 | 内容 | ポイント |
|------|------|----------|
| 0:00-0:25 | 環境構築とセットアップ | 開発の準備を整えよう |
| 0:25-0:40 | Human-in-the-Loop 開発の体験 | AI との対話方法を学ぼう |
| 0:40-1:10 | Issue 駆動開発の実践 | タスクを分解して進めよう |
| 1:10-1:45 | TDD で API 開発 | テストを書きながら開発しよう |
| 1:45-2:00 | 完成とまとめ | 動くアプリを確認しよう |

---

## 🛠️ Part 1: 環境構築（25分）

開発を始める前に、必要なツールをインストールしましょう。コピー＆ペーストで進められるので安心してください。

**📝 対象OS**: このワークショップはmacOSを対象としています。

### 1.1 uv のインストール（オールインワン開発ツール）

uv は最新の Python 開発ツールです。Python のインストールからパッケージ管理まで、すべてを一括で扱えます。

ターミナル（Terminal.app）を開いて、以下のコマンドを実行しましょう。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

インストール後、新しいターミナルウィンドウを開いて確認します。

```bash
uv --version
```

**💡 ポイント**：uv があれば、Python を個別にインストールする必要はありません。プロジェクトに必要な Python バージョンは自動的に管理されます。

### 1.2 Homebrew のインストール

まず、パッケージマネージャーの Homebrew をインストールします。

```bash
# Homebrew のインストール
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**インストール後、パスを通す設定:**

**Apple Silicon Mac (M1/M2/M3) の場合:**

```bash
# 設定ファイルに空行を追加
echo >> ~/.zprofile
# 設定ファイルにパスを追加
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
# 現在のセッションにパスを適用
eval "$(/opt/homebrew/bin/brew shellenv)"
```

**Intel Mac の場合:**

```bash
# 設定ファイルに空行を追加
echo >> ~/.zprofile
# 設定ファイルにパスを追加
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
# 現在のセッションにパスを適用
eval "$(/usr/local/bin/brew shellenv)"
```

**Homebrew が正常にインストールされたか確認:**

```bash
brew --version
```

**📋 インストール中の操作手順:**

1. **パスワード入力が求められます**:

   ```text
   Password:
   ```

   👉 **macOSのログインパスワードを入力してください**（入力中は文字が表示されません）

2. **確認メッセージが表示されます**:

   ```text
   Press RETURN/ENTER to continue or any other key to abort:
   ```

   👉 **Enterキーを押して続行してください**

3. **インストールが進行します**（数分かかる場合があります）

4. **インストール完了後**、Homebrewが表示する指示に従ってパス設定を行ってください
   - 通常、以下のような指示が表示されます：

   ```text
   Next steps:
   - Run these commands in your terminal to add Homebrew to your PATH:
   ```

   - お使いのMacに応じて上記のパス設定コマンドを実行してください

⚠️ **注意**:

- **Macの種類の確認**: `uname -m` コマンドで確認できます
  - `arm64` → Apple Silicon Mac
  - `x86_64` → Intel Mac
- **コマンド順序**: `echo >>`で空行追加 → `echo 'eval...'`でパス設定追加 → `eval`で現在のセッションに適用
- `.zprofile` は macOS のターミナル設定ファイルです。ここにパス設定を書くことで、新しいターミナルウィンドウでも `brew` コマンドが使えるようになります。
- パスワード入力時は、セキュリティ上の理由で文字が画面に表示されませんが、正常に入力されています。

### 1.3 Git と GitHub CLI のセットアップ

**macOS の場合：**

```bash
# Git のバージョン確認（macOS には標準でインストール済み）
git --version

# Homebrew を最新に更新してから GitHub CLI をインストール
brew update
brew install gh

# GitHub にログイン
gh auth login
```

`gh auth login` の詳細手順：

1. **GitHub.com** を選択
2. **HTTPS** を選択  
3. **Y**（ブラウザで認証）を選択
4. **認証方法選択画面が表示されます**：

   ```text
   > Login with a web browser
     Paste an authentication token
   ```

   👉 **そのままEnterキーを押してください**（Login with a web browserが選択されている状態）

5. **ワンタイムコードが表示されます**：

   ```text
   ! First copy your one-time code: XXXX-XXXX
   Press Enter to open https://github.com/login/device in your browser...
   ```

   👉 **コードをメモして、Enterキーを押してください**

6. **ブラウザが開いて認証ページが表示されます**
   - コードを入力してGitHubアカウントでログイン
   - 認証完了後、ターミナルに戻って「Authentication complete!」が表示されます

### 1.4 Cursor のインストール

#### インストール手順

1. **ダウンロード**
   - [cursor.com](https://cursor.com) にアクセス
   - 「Download」ボタンをクリック
   - macOS に対応したインストーラーが自動的にダウンロード

2. **インストール実行**
   - ダウンロードしたファイルを開いてインストール
   - インストール完了まで待機

3. **Cursor の起動**
   - デスクトップショートカットまたはアプリケーションメニューから起動

#### 初期設定

初回起動時に以下の設定を行います。

1. **ログイン方法の選択**
   - **GitHub アカウントで**サインイン

2. **エディター設定**
   - キーボードショートカット（以前使用していたエディターと合わせる）
   - テーマの選択（Dark/Light）
   - VS Code から設定をインポート（該当する場合）

3. **AI 機能の設定**
   - AI との対話言語の設定
   - コードベースのインデックス設定
   - プライバシー設定

4. **CLI ショートカット**
   - ターミナルから Cursor を起動するためのコマンド設定

**💡 ポイント**：

- Cursor Pro の 14 日間無料トライアル付き
- 初期設定は後から変更可能
- VS Code の設定や拡張機能も移行可能

### 1.5 プロジェクトの準備

テンプレートリポジトリから自分のプロジェクトを作成します。

```bash
# ブラウザでテンプレートリポジトリを開く
open https://github.com/asakaguchi/cursor-workshop-template
```

または、ブラウザで直接 <https://github.com/asakaguchi/cursor-workshop-template> にアクセスしてください。

GitHubページで以下の手順を実行します。

1. **「Use this template」ボタンをクリック**（緑色のボタン）
2. **「Create a new repository」を選択**
3. **Repository name**: `my-product-api`（またはお好きな名前）
4. **Description**: 「Cursor workshop - Product API」（任意）
5. **Public/Private**: Public を推奨（学習目的のため）
6. **「Include all branches」**: チェックしない（デフォルト）
7. **「Create repository」をクリック**

⚠️ **注意**: リポジトリの作成には数秒かかる場合があります。

次に、作成したリポジトリをローカルにクローンします。

**💡 ベストプラクティス**：開発プロジェクトは `~/Projects` ディレクトリで管理しましょう。デスクトップではなく専用ディレクトリを使うことで、プロジェクトの整理と管理が容易になります。

```bash
# 開発用ディレクトリを作成・移動
mkdir -p ~/Projects
cd ~/Projects

# 自分のリポジトリをクローン（YOUR_USERNAME は自分の GitHub ユーザー名）
git clone https://github.com/YOUR_USERNAME/my-product-api.git
cd my-product-api

# 依存関係を同期（uv が必要な Python も自動インストール）
uv sync

# Cursor で開く
cursor .
```

**💡 ポイント**：テンプレートリポジトリを使うことで、必要なファイルがすべて揃った状態から始められます。`uv sync` で Python と全パッケージが自動的にセットアップされます。

---

## 🤝 Part 2: Human-in-the-Loop 開発を体験（15 分）

### 2.1 Cursor の AI 機能を理解しよう

Cursor には主に3つのAI機能があります：

1. **チャット（Cmd+L）**：AI と対話しながら開発
2. **インライン編集（Cmd+K）**：コードを直接編集
3. **Composer（Cmd+I）**：複数ファイルの同時編集

今日は主に**チャット機能**を使います。

### 2.2 最初のAIとの対話

1. **Cmd+L** を押してチャットパネルを開く
2. 以下のメッセージを入力してみましょう。

```text
@requirements.md を読んで、どんなアプリを作るのか教えてください。
初心者にもわかりやすく説明してください。
```

AI が要件を説明してくれます。わからない用語があれば、続けて質問してみましょう。

```text
API って何ですか？もっと簡単に説明してください。
```

### 2.3 Cursor Rulesの確認

プロジェクトには「Cursor Rules」という開発ルールが設定されています：

```text
.cursor/rules/ にあるファイルを見て、このプロジェクトの開発ルールを
箇条書きでまとめてください。
```

**💡 ポイント**：AI は常にこれらのルールに従って回答してくれます。

---

## 📝 Part 3: Issue 駆動開発の実践（30 分）

### 3.1 タスクの分解を依頼

大きなタスクを小さく分解することで、開発が進めやすくなります。AI に以下を依頼してみましょう。

```text
@requirements.md @.cursor/prompts/task-breakdown.md

要件を確認して、2 時間で完成できるようにタスクを分解してください。
各タスクは 15-30 分で完了できる粒度にしてください。
```

⚠️ **トラブルシューティング**: task-breakdown.md ファイルがない場合は、以下で代用してください。

```text
@requirements.md を読んで、2 時間で完成できるようにタスクを分解してください。
各タスクは 15-30 分で完了できる粒度にしてください。
```

AI がタスク一覧を提示してくれます。

### 3.2 GitHub Issue の作成

タスクが承認できたら、シンプルに返答しましょう。

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

**💡 ポイント**：各 Issue には番号（#1, #2 など）が付いています。これがタスクの識別子になります。

---

## 🧪 Part 4: TDD で API 開発（30 分）

### 4.1 最初のタスク開始

AI に最初のタスクを始めることを伝えます：

```text
Task 1 を開始してください
```

AI が自動的に：

1. 新しいブランチを作成
2. 必要なファイルを作成
3. テストを先に書く（TDD）

### 4.2 TDD のサイクルを体験

TDD（テスト駆動開発）は以下の 3 ステップで進めます。

1. **Red**：失敗するテストを書く
2. **Green**：テストを通す最小限のコード
3. **Refactor**：コードを改善

AI がこのサイクルを実践して見せてくれます。

### 4.3 テストの実行

```bash
# テストを実行
uv run pytest tests/ -v

# 特定のテストだけ実行
uv run pytest tests/test_basic.py -v
```

**💡 ポイント**：最初は赤い文字（失敗）が表示され、コードを書くと緑（成功）になります。

### 4.4 プルリクエストの作成

タスクが完了したら、AIに伝えましょう。

```text
Task 1 が完了しました。PR を作成してください。
```

AIが以下の作業を自動で行います。

1. コードをコミット
2. GitHub にプッシュ
3. プルリクエストを作成

---

## 🎉 Part 5: 完成とまとめ（15 分）

### 5.1 API の動作確認

全てのタスクが完了したら、実際に API を動かしてみましょう。

```bash
# 依存関係を同期
uv sync

# API サーバーを起動
uv run uvicorn product_api.main:app --reload --port 8000

# 別のターミナルで商品を作成
curl -X POST "http://localhost:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "テスト商品", "price": 1000}'

# 作成した商品を取得
curl -X GET "http://localhost:8000/items/1"
```

### 5.2 Swagger UI で確認

ブラウザで <http://localhost:8000/docs> にアクセスすると、API の仕様が視覚的に確認できます。

### 5.3 学んだことの振り返り

今日体験したことをまとめましょう。

✅ **Human-in-the-Loop開発**

- AI と対話しながら開発
- 人間が方向性を決め、AI が実装

✅ **Issue 駆動開発**

- タスクを小さく分解
- 進捗が見える化

✅ **TDD（テスト駆動開発）**

- バグの少ないコード
- 安心して修正できる

✅ **プロ同様の開発フロー**

- Git/GitHub でバージョン管理
- プルリクエストでコードレビュー

---

## 🚀 次のステップ

### さらに学ぶには

1. **機能追加に挑戦**
   - 商品の更新（PUT）
   - 商品の削除（DELETE）
   - 商品一覧の取得（GET /items）

2. **データベース連携**
   - SQLite を使った永続化
   - SQLAlchemy の導入

3. **認証機能の追加**
   - JWT トークン認証
   - ユーザー管理

### 役立つリソース

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)
- [Cursor公式ドキュメント](https://docs.cursor.com/)
- [GitHub Skills](https://skills.github.com/)

---

## 💡 トラブルシューティング

### よくある問題と解決法

#### Q: uv コマンドが見つからない

```bash
# パスを通す
source ~/.zshrc  # または source ~/.bashrc
```

#### Q: ポート 8000 が使用中

```bash
# 別のポートで起動
uv run uvicorn product_api.main:app --reload --port 8001
```

#### Q: テストが失敗する

```bash
# 依存関係を再同期
uv sync --dev
```

#### Q: Cursor が重い

- 設定 → Performance → 「Code Index」をオフ
- 不要な拡張機能を無効化

---

## 🎓 おめでとうございます

2時間でプログラミングの基礎から API の完成まで体験できました。これはプロの開発者が日々行っている実際のワークフローです。

最も重要なのは、**完璧を求めず、AI と協力しながら前進すること**です。わからないことがあれば、遠慮なく AI に質問してください。

Happy Coding! 🎉
