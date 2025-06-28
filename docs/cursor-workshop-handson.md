# Cursor×Python×GitHub ハンズオン

## AI と一緒にプログラミングを始めよう

### 今日のゴール

プログラミング未経験でも大丈夫です。今日は以下のことができるようになります。

1. **AI ペアプログラミング**：Cursor を使って AI と対話しながらコードを書く
2. **プロジェクト管理**：GitHub でタスクを管理し、コードを共有する
3. **品質の高いコード**：テストを書きながら安心して開発を進める
4. **動くアプリ完成**：商品管理 API と Web UI を作り上げる

難しそうに聞こえるかもしれません。でも大丈夫、AI がずっと隣にいてサポートしてくれます。

---

## タイムスケジュール（1.5時間）

| 時間 | 内容 | ポイント | AI ペアプロ効果 |
|------|------|----------|----------------|
| 0:00-0:20 | 環境構築とセットアップ | 開発の準備を整えよう | AI診断で高速トラブル解決 |
| 0:20-0:30 | Human-in-the-Loop 開発の体験 | AI との対話方法を学ぼう | 実践重視で要点集約 |
| 0:30-0:45 | Issue 駆動開発の実践 | タスクを分解して進めよう | AI が一括でタスク管理 |
| 0:45-1:00 | TDD で API 開発 | テストを書きながら開発しよう | AI が高速実装・テスト |
| 1:00-1:15 | Web UI 開発 | Streamlit で画面を作ろう | AI が UI設計から実装まで |
| 1:15-1:25 | Cloud Run デプロイ | クラウドで本格運用しよう | **MCP で自動デプロイ** |
| 1:25-1:30 | 完成とまとめ | 本格アプリの完成を確認 | 全機能統合確認 |

---

## Part 1：環境構築（20分）

**AI ペアプロ効果**：トラブルシューティングを AI が即座に診断し、Docker ビルド中に次のステップを AI と相談できるため5分短縮可能。

開発を始める前に、必要なツールをインストールしましょう。コピー＆ペーストで進められるので安心してください。

**対象OS**：このワークショップは macOS を対象としています。

**開発環境**：このワークショップでは Docker を使用します。

- 環境差異がなく、確実に動作します
- 依存関係の問題が起こりません
- VS Code Dev Container で快適な開発体験を実現できます

### 1.1 Cursor のインストール

#### インストール手順

1. **ダウンロード**
   - [cursor.com](https://cursor.com) にアクセス
   - 「ダウンロード MacOS」ボタンをクリック
   - ファイル名やダウンロード先を確認（必要に応じて変更）して「保存」ボタンをクリック

2. **インストール実行**
   - ダウンロードしたファイルを開く
   - Cursor アイコンを Application アイコンにドラッグ＆ドロップ

3. **Cursor の起動**
   - Launchpad から Cursor を起動

#### 初期設定

初回起動時に以下の設定を行います。

1. **ログイン方法の選択**
   - **GitHub アカウントで**サインイン
2. **エディター設定**
   - テーマのカスタマイズ
   - キーバインドの設定
   - データ共有事項についての内容を確認し、チェックボックスをオンにし、「Continue」ボタンをクリック
     （デフォルトでは、データが学習に使われる設定になっているので、学習されないように後で設定を変更する）
   - 言語設定とターミナルコマンドの設定
     - Language for AI → Japanese
     - Open from Terminal → `cursor` command → 「Install」ボタンをクリック
     - 「Continue」ボタンをクリック
3. **プライバシー設定**
   - 右上の歯車アイコンをクリック
   - 「General」→「Privacy」→「Privacy Mode with Storage」に変更
4. **Japanese Language Pack 拡張機能のインストール**
   - 拡張機能を開く（`Cmd`+`Shift`+`X`）
   - 入力欄に、`Japanese` と入力
   - `Japanese Language Pack for Visual Studio Code` 拡張機能の `Install` ボタンをクリック
   - 画面左下に、`Would you like to change Cursor's display language to Japanese and restart?` とメッセージが表示されたら、そこに表示されている `Change Language and Restart` ボタンをクリック

【ポイント】

- Cursor Pro の 14 日間無料トライアル付きです
- 初期設定は後から変更可能です
- VS Code の設定や拡張機能も移行可能です

### 1.2 Docker Desktop のインストール

1. [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/) にアクセス
2. 「Download Docker Desktop」にマウスカーソルを合わせる
   - Apple Silicon Mac（M1/M2/M3）：「Download for Mac - Apple Silicon」をクリック
   - Intel Mac：「Download for Mac - Intel Chip」をクリック
3. ファイル名やダウンロード先を確認（必要に応じて変更）して「保存」ボタンをクリック
4. ダウンロードしたファイルを開く
5. Docker アイコンを Application アイコンにドラッグ＆ドロップ
6. Launchpad から Docker を起動
7. Docker Subscription Service Agreement の画面で、「Accept」ボタンをクリック
8. 「Use recommended settings (requires password)」を選択し、「Finish」ボタンをクリック
   - macOS アカウントのパスワードを入力
9. Welcome to Docker の画面で、「Skip」リンクをクリック
10. Welcome Survey の画面で、「Skip」リンクをクリック

動作確認を行います。

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
2. **「Create a new repository」を選択**
3. **Repository name**：`my-cursor-workshop`（またはお好きな名前）
4. **「Create repository」をクリック**

リポジトリの作成には数秒かかる場合があります。

次に、作成したリポジトリをローカルにクローンし、Cursor で開きます。

【ベストプラクティス】
開発プロジェクトは `~/Projects` ディレクトリで管理することを推奨します。デスクトップではなく専用ディレクトリを使うことで、プロジェクトの整理と管理が容易になります。

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
2. コマンドパレットを開く（`Cmd`+`Shift`+`P`）
3. 「`Dev Containers: Reopen in Container`」と入力して選択
   一部入力すると候補が表示されるので、候補の中に「`Dev Containers: Reopen in Container`」が表示されたらそれをクリック
4. 初回は Docker イメージのビルドに数分かかります
   ネットワーク環境やマシンスペックにより 5-15 分程度かかる場合があります。
   コーヒーでも飲みながら待ちましょう。
5. 完了すると、ターミナルが表示されます

### 1.5 GitHub CLI の認証設定

開発の準備として、GitHub CLI の認証を済ませておきます。

開いているターミナルで、以下のコマンドを入力します。

```bash
gh auth login
```

認証プロンプトが表示されたら、以下の手順で認証を進めます。

1. **What account do you want to log into?** → `GitHub.com` を選択し、`ENTER` キーを押す
2. **What is your preferred protocol for Git operations?** → `HTTPS` を選択し、`ENTER` キーを押す
3. **Authenticate Git with your GitHub credentials?** → `ENTER` キーを押す
4. **How would you like to authenticate GitHub CLI?** → `Login with a web browser` を選択し、`ENTER` キーを押す
5. **Press Enter to open github.com in your browser...** → `Enter` キーを押す
6. ブラウザが開くので、表示されたワンタイムコードを入力
7. GitHub にログインして認証を完了

【ポイント】

- 認証は **Part 3（Issue 駆動開発）の前まで** に完了すれば OK です
- 基本的な `git` コマンド（add、commit 等）は認証なしでも動作します
- GitHub CLI 機能（Issue 作成、PR 作成等）には認証が必要です

【Dev Container の利点】

- Python、uv、必要なツールがすべてインストール済みです
- Cursor の拡張機能も自動でインストールされます
- チーム全員が同じ環境で開発可能です

テンプレートリポジトリを使うことで、必要なファイルがすべて揃った状態から始められます。Dev Container を使用することで、Python とすべての開発ツールが自動的にセットアップされます。

【できたこと】

- 開発環境の構築が完了
- AI と一緒に開発する準備が整った

---

## Part 2：Human-in-the-Loop 開発を体験（10分）

**AI ペアプロ効果**：理論説明を最小化し、実際の AI との対話体験に集中することで5分短縮。AI が即座に質問に回答するため学習効率が大幅向上。

### 2.1 Cursor の AI 機能を理解しよう

Cursor には主に 3 つの AI 機能があります。

1. **チャット（Cmd+L）**：AI と対話しながら開発
2. **インライン編集（Cmd+K）**：コードを直接編集
3. **Composer（Cmd+I）**：複数ファイルの同時編集

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

【ポイント】

- AI は常にこれらのルールに従って回答してくれます
- このプロジェクトはモダンな **src レイアウト**を採用しています（コードは `src/product_api/` に配置）

これらのルールにより、AI は常に以下を実現してくれます。

- 一貫したコーディングスタイルを維持
- ベストプラクティスに従った実装
- プロジェクト固有の規約を遵守

---

## Part 3：Issue 駆動開発の実践（15分）

**AI ペアプロ効果**：AI がタスク分解から GitHub Issue 作成まで一括実行。人間の「ok」一言で AI が GitHub 連携を自動完遂するため5分短縮。

### 3.1 タスクの分解を依頼

大きなタスクを小さく分解することで、開発が進めやすくなります。AI に以下を依頼してみましょう。

```text
@requirements.md @.cursor/prompts/task-breakdown.md

要件を確認して、2 時間で完成できるようにタスクを分解してください。
各タスクは 15-30 分で完了できる粒度にしてください。
```

`@.cursor/prompts/task-breakdown.md` ファイルは、タスク分解の具体的なガイドラインを提供します。このファイルを参照することで、AI がより適切にタスクを分解してくれます。

AI がタスクの一覧を提示してくれます。

### 3.2 GitHub Issue の作成

タスクの内容を確認して問題なければ、シンプルに返答しましょう。

```text
ok
```

と入力するだけで、AI が自動的に GitHub Issue を作成してくれます。

### 3.3 Issue の確認

ブラウザで以下を確認します。

```bash
gh repo view --web
```

「Issues」タブを見ると、作成されたタスクが一覧で見えます。

各 Issue には番号（#1、#2 など）が付いており、これがタスクの識別子になります。

【できたこと】

- タスクの分解と可視化が完了
- GitHub でプロジェクト管理の準備が整った

---

## Part 4：TDD で API 開発（15分）

**AI ペアプロ効果**：AI が Red-Green-Refactor サイクルを高速実行。人間の10-20倍の実装速度でテスト実行と次の実装を並行処理するため5分短縮。

Dev Container 使用時の注意点です。以降のコマンドは Dev Container 内で実行されるため、`docker compose exec app` を省略して直接コマンドを実行できます。Dev Container のターミナルは、すでにコンテナ内部で動作しています。

### 4.1 最初のタスク開始

AI に最初のタスクを始めることを伝えます。

```text
Task 1 を開始してください
```

AI が以下の作業を自動で進めます。

1. 新しいブランチを作成
2. 必要なファイルを作成（`src/product_api/` 配下に配置）
3. テストを先に書く（TDD）

### 4.2 TDD のサイクルを体験

TDD（テスト駆動開発）は以下の 3 ステップで進めます。

1. **Red**：失敗するテストを書く
2. **Green**：テストを通す最小限のコード
3. **Refactor**：コードを改善

AI がこのサイクルを実践しながら開発を進めます。

### 4.3 テストの実行

Dev Container 内では以下のコマンドを直接実行できます。

```bash
# テストを実行（カバレッジ付き）
uv run pytest

# 詳細出力でテスト実行
uv run pytest -v

# 特定のテストだけ実行
uv run pytest tests/test_specific.py -v
```

Dev Container 環境では、すでにコンテナ内にいるため `docker compose exec app` は不要です。

最初は赤い文字（テスト失敗）が表示され、実装を進めると緑（テスト成功）に変わります。

### 4.4 プルリクエストの作成

【タスク完了の目安】

- すべてのテストが緑色（成功）になった
- コードが期待通りに動作している
- リファクタリングが必要なら完了している

タスクが完了したら、AI に伝えましょう。

```text
Task 1 が完了しました。PR を作成してください。
```

AI が以下の作業を自動で進めます。

1. コードをコミット
2. GitHub にプッシュ
3. プルリクエストを作成

【できたこと】

- TDD で品質の高いコードを実装
- GitHub でコードレビューの準備が完了

---

## Part 5：Web UI 開発（15分）

**AI ペアプロ効果**：AI がプロダクトマネージャーとして要件整理から UI 設計、TDD 実装まで一貫して実行。適切なモックを使った UI テストも AI が自動生成するため15分の大幅短縮。

商品管理APIが完成したら、次は Web UI の開発に挑戦します。Streamlitを使用して、APIを操作するための使いやすいインターフェースを構築します。

### 5.1 AI との要件定義

まず、AI にプロダクトマネージャーとして振る舞ってもらい、UI の要件を定義します。

```text
商品管理APIを操作するためのWeb UIを、Streamlitを使って作成したい。

あなたは経験豊富なプロダクトマネージャーとして、このUIにどんな画面や機能があると便利か、アイデアをいくつか提案して欲しい。ターゲットユーザーは、商品の在庫を管理する社内の担当者です。
```

AI が提案する機能の中から、**実装済みのAPIで実現可能なもの**だけに絞り込みます。

### 5.2 仕様書の作成

現実的な開発では、全ての機能を一度に実装することはできません。最小限の機能から始めることが重要です。

```text
今回は、実装済みのAPIのみに絞って開発を進めたい。機能要件をまとめて仕様書として @/docs に作成してください。
```

この段階で、以下の点を明確にしておきます。

- 利用可能なAPIエンドポイント
- 実装する画面と機能
- 実装しない機能とその理由

### 5.3 TDD の重要性

Web UI 開発でも TDD は必須です。プロジェクトのガイドラインには以下が明記されています。

```text
### 3. テスト要件（t-wada方式TDD）
- **TDD厳守**: 実装前に必ず失敗するテストを書く
- **1テスト1アサーション**: アサーションルーレットを避ける
- **新機能にはテスト必須**: Red-Green-Refactorサイクルで実装
- **テストファースト**: テストなしのコードは絶対に書かない
```

### 5.4 TDD を怠った場合の問題

もし TDD を実践しなかった場合、以下のような問題が発生します。

【技術的な問題】

- バグの発見が遅れる
- リファクタリングが困難になる
- 品質の保証ができない

【プロセス的な問題】

- ガイドライン違反による信頼性の低下
- チーム内での一貫性の欠如
- 技術的負債の蓄積

「UIだから」「時間がないから」という理由で TDD を省略してはいけません。Streamlit のような UI フレームワークでも、適切なモック（模擬オブジェクト）を使用してテストを書くことができます。

### 5.5 Web UI タスクの実行

タスクの内容を確認したら、実装を開始します。

```text
ok
```

各タスクは以下の流れで進めます。

1. **テストを書く**（Red）
2. **最小限の実装**（Green）
3. **リファクタリング**（Refactor）
4. **動作確認**
5. **コミットとPR作成**

この流れを確実に守ることで、品質の高いコードを維持できます。

### 5.6 動作確認

Web UI の実装が完了したら、実際に動かしてみましょう。

```bash
# Streamlit UI を起動
uv run streamlit run src/product_ui/main.py
```

ブラウザで <http://localhost:8501> にアクセスすると、作成した UI を確認できます。

---

## Part 6：Cloud Run デプロイ（10分）

**AI ペアプロ効果**：Cloud Run MCP を活用して AI が Docker ビルド、イメージプッシュ、Cloud Run サービス作成まで自動実行。本格的なクラウドデプロイを短時間で実現。

### 6.1 AI によるクラウドデプロイ（5分）

Web UI の実装が完了したら、いよいよクラウドデプロイに挑戦です。AI に以下を依頼してみましょう。

```text
Cloud Run にデプロイして本格運用環境を構築してください
```

AI が以下の作業を自動で進めます：

1. **Docker イメージのビルド**：`docker/Dockerfile` を使用
2. **Google Container Registry へプッシュ**：イメージを GCR に保存
3. **Cloud Run サービス作成**：本番環境での API 公開
4. **URL の提供**：デプロイされた API の URL を取得

【重要な前提条件】

- `docs/cloud-run-mcp-setup.md` の設定が完了していること
- Google Cloud プロジェクトの認証が済んでいること
- Cloud Run MCP (`.mcp.json`) が設定済みであること

### 6.2 本番環境での動作確認（5分）

デプロイが完了したら、本格的なクラウド環境で動作確認を行います。

#### API の動作確認

AI が提供した Cloud Run URL で以下を確認：

```bash
# ヘルスチェック（Cloud Run URL に置き換え）
curl https://your-app-name-xxxxx.a.run.app/health

# Swagger UI にアクセス
open https://your-app-name-xxxxx.a.run.app/docs
```

#### 本番環境での商品管理テスト

Swagger UI を使って以下の操作を実行：

1. **商品作成**：POST /items エンドポイントで新しい商品を登録
2. **商品取得**：GET /items/{id} エンドポイントで登録した商品を取得
3. **エラーハンドリング**：無効なデータでバリデーションをテスト

#### Web UI からクラウド API への接続（時間に余裕があれば）

ローカルの Streamlit UI からクラウドの API への接続を確認：

```bash
# Streamlit UI を起動（API_BASE_URL を Cloud Run URL に設定）
export API_BASE_URL=https://your-app-name-xxxxx.a.run.app
uv run streamlit run src/product_ui/main.py
```

【できたこと】

- 本格的なクラウド環境での API 運用
- インターネット経由でのアクセス確認
- スケーラブルな本番環境の構築

---

## Part 7：完成とまとめ（5分）

**AI ペアプロ効果**：ローカル開発からクラウドデプロイまでの完全な開発フローを1.5時間で実現。AI との協働により従来の数倍の効率で本格アプリを完成。

### 7.1 最終確認

以下が完成していることを確認します：

1. **ローカル開発環境**：Docker + Dev Container
2. **商品管理 API**：FastAPI による REST API
3. **Web UI**：Streamlit による操作画面
4. **クラウドデプロイ**：Google Cloud Run での本番運用
5. **品質保証**：TDD による堅牢なテストコード

### 7.2 学んだことの振り返り

今日体験したことをまとめましょう。

【Human-in-the-Loop 開発】

- AI と対話しながら開発
- 人間が方向性を決め、AI が実装

【Issue 駆動開発】

- タスクを小さく分解
- 進捗が見える化

【TDD（テスト駆動開発）】

- バグの少ないコード
- 安心して修正できる

【実践的な開発フロー】

- Git/GitHub でバージョン管理
- プルリクエストでコードレビュー

【Web UI 開発】

- UI でも TDD は必須
- ガイドライン厳守の重要性

【Cloud Run デプロイ】

- MCP による自動デプロイ
- 本格的なクラウド運用の実現

【AI ペアプログラミングの威力】

- 開発効率の劇的向上（従来の数倍の速度）
- 高品質なコードの自動生成
- 複雑な設定の自動化

---

## 次のステップ

### さらに学ぶには

【機能追加に挑戦】

- 商品の更新（PUT）
- 商品の削除（DELETE）
- 商品一覧の取得（GET /items）

【データベース連携】

- SQLite を使った永続化
- SQLAlchemy の導入

【認証機能の追加】

- JWT トークン認証
- ユーザー管理

【UI の拡張】

- より高度な検索機能
- データ可視化
- エクスポート機能

### 役立つリソース

- [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)
- [Cursor公式ドキュメント](https://docs.cursor.com/)
- [GitHub Skills](https://skills.github.com/)
- [Streamlit公式ドキュメント](https://docs.streamlit.io/)

---

## トラブルシューティング

エラーは学習のチャンスです。プログラミングではエラーは日常茶飯事です。エラーメッセージは「何が問題か」を教えてくれる大切な情報です。

焦らず、以下の解決法を試してみましょう。

### よくある問題と解決法

#### Q：コメント行でエラーが出る

```text
zsh: command not found: #
```

【解決法】
コメント行（`#` で始まる行）は実行しないでください。コードブロック内のコマンドのみ実行してください。

#### Q：「brew install sh」でエラーが出る

```text
Warning: No available formula with the name "sh". Did you mean shc?
```

【解決法】
正しくは `brew install gh` です。`sh` ではなく `gh` (GitHub CLI) をインストールしてください。

#### Q：警告メッセージが表示される

```text
WARN: The following commands are shadowed by other commands in your PATH: uv uvx
```

【解決法】
既存のツールがあることを示す警告です。問題ありません。そのまま続行してください。

#### Q：GitHub CLI の更新通知が表示される

```text
A new release of gh is available: 2.74.0 → 2.74.1
To upgrade, run: brew upgrade gh
```

【解決法】
更新は任意です。ハンズオン中は無視して構いません。後で `brew upgrade gh` で更新できます。

### Docker 関連のトラブルシューティング

#### Q：Docker Desktop が起動していない

```text
Cannot connect to the Docker daemon at unix:///var/run/docker.sock.
```

【解決法】
Docker Desktop アプリケーションを起動してください。メニューバーに Docker アイコンが表示されます。

#### Q：Docker コンテナのポートが使用中

```text
bind: address already in use
```

【解決法】

```bash
# 使用中のコンテナを停止
docker compose down

# または別のポートを使用
# compose.yml を編集して "8000:8000" を "8001:8000" に変更
```

#### Q：Cursor で "Reopen in Container" が表示されない

【解決法】

1. Cursor に Dev Containers 拡張機能をインストール
2. 拡張機能を検索："ms-vscode-remote.remote-containers"
3. インストール後、Cursor を再起動

#### Q：Cursor Pyright 設定のインポートについて

Dev Container 起動時に「Would you like Cursor Pyright to import your settings from Pylance?」というダイアログが表示される場合があります。

【推奨回答】
**「No」を選択**

【理由】

- このプロジェクトには既に最適化された Pyright 設定が `pyproject.toml` で定義済みです
- Pylance からの設定をインポートすると、プロジェクト固有の設定が上書きされる可能性があります
- プロジェクトの一貫性を保ち、トラブルシューティングを簡素化するため

「Never ask again」もチェックして、今後同様のダイアログを非表示にすることを推奨します。

#### Q：Docker コンテナ内でコマンドが実行できない

【Dev Container を使用している場合】

ターミナルはすでにコンテナ内で動作しているため、直接コマンドを実行できます。

```bash
# Dev Container のターミナルで直接実行
uv run pytest
```

【Dev Container を使用していない場合】

```bash
# コンテナに入る
docker compose exec app bash

# または直接コマンドを実行
docker compose exec app uv run pytest
```

#### Q：Docker イメージのビルドが遅い

【解決法】

- 初回ビルドは時間がかかります（約 5-10 分）
- 2 回目以降はキャッシュが利用されるため高速化されます
- Docker Desktop の設定でメモリを増やすことで改善する場合があります

### Web UI 開発のトラブルシューティング

#### Q：商品作成画面でプレビューが反映されない

【症状】
商品名や金額を入力してもプレビューが「未入力」と表示される。

【原因】
Streamlitの`st.form`の仕様により、フォーム内の入力値は送信ボタンが押されるまで他のコンポーネントからアクセスできません。

【解決法】
フォーム内でのリアルタイムプレビューではなく、フォーム外での入力とセッション状態管理を使用します。

#### Q：TDD でテストが書けない

【よくある誤解】
「UIのテストは難しい」「時間がない」

【正しい対処法】

```python
# tests/test_ui_components.py
import pytest
from unittest.mock import Mock, patch

def test_product_form_validation():
    """商品フォームのバリデーションをテスト"""
    # Red: まずテストを書く
    with patch('streamlit.text_input') as mock_input:
        mock_input.return_value = ""  # 空の入力
        
        # バリデーション関数を呼び出し
        error = validate_product_name("")
        
        # エラーが返ることを確認
        assert error == "商品名は必須です"
```

UIのテストも適切なモックを使用すれば十分に可能です。

---

## おめでとうございます

2 時間でプログラミングの基礎から API と Web UI の完成まで体験できました。これはプロの開発者が日々行っている実際のワークフローです。

最も重要なのは、**完璧を求めずに AI と協力しながら前進すること**です。わからないことがあれば、遠慮なく AI に質問してください。

Happy Coding!
