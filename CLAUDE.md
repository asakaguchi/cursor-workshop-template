# CLAUDE.md

このファイルは、このリポジトリのコードを扱う際のClaude Code (claude.ai/code)のためのガイダンスを提供します。

## 言語処理の指示

**注意**: Cursorエディタを使用する場合は、`.cursor/rules/`ディレクトリのルールファイルも参照してください。特に以下が重要です：

- `python-structure.mdc`: モダンなPythonプロジェクト構造（srcレイアウト）
- `code-quality-enforcement.mdc`: コード品質と開発ガイドライン
- `development-workflow.mdc`: 開発フローとGitHub統合
- `pep8-enforcement.mdc`: Pythonコーディング標準

## 参考資料

このプロジェクトは以下のリソースに基づいて構築されています：

- **記事**: [DockerでモダンなPython開発環境を構築する](https://zenn.dev/mjun0812/articles/0ae2325d40ed20)
- **テンプレート**: [mjun0812/python-project-template](
  https://github.com/mjun0812/python-project-template)
  - 特に[CLAUDE.md](
    https://github.com/mjun0812/python-project-template/blob/main/CLAUDE.md)の構造を参考にしています

uvの使用、プロジェクト構造など多くの要素が上記のリソースに基づいています。

## プロジェクト概要

これはPythonとFastAPIを使用して**商品管理API**を構築するためのCursorワークショップテンプレートです。インメモリストレージを使用したシンプルなREST APIを実装します。

## 主要な要件

APIは以下を実装する必要があります：

- 商品作成（POST /items）
- 商品取得（GET /items/{id}）
- ヘルスチェック（GET /health）
- pytestを使用したTDDアプローチ
- 自動Swagger UI生成を備えたFastAPIフレームワーク

### 商品データ構造

- id: 整数（自動生成）
- name: 文字列（必須、最低1文字）
- price: 浮動小数点数（必須、0より大きい）
- created_at: 日時（自動設定）

## 開発コマンド

### 初回セットアップ

```bash
# Python仮想環境のセットアップ
uv sync

# 仮想環境を有効化
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### パッケージ管理

**重要**: 常にuvを使用し、pipは決して使用しないでください

```bash
# プロジェクトの同期（推奨 - pyproject.tomlから自動認識）
uv sync

# 必要に応じて新しい依存関係を追加する場合のみ
# uv add package_name
# uv add --dev dev_package_name
```

### アプリケーションの実行

```bash
# FastAPIサーバーの起動
uvicorn src.product_api.main:app --reload

# Swagger UIへのアクセス: http://localhost:8000/docs
```

### テスト

```bash
# すべてのテストを実行
uv run --frozen pytest

# 特定のテストファイルを実行
uv run --frozen pytest tests/test_filename.py

# 詳細出力でテストを実行
uv run --frozen pytest -v

# anyioプラグインの問題がある場合
PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest
```

### コード品質チェック

```bash
# コードフォーマット
uv run --frozen ruff format .

# Lintチェック
uv run --frozen ruff check .

# Lint問題の修正
uv run --frozen ruff check . --fix

# 型チェック
# 手動で実行する場合：
uv run --frozen pyright

# Markdownファイルのチェック（必須）
markdownlint *.md

# pre-commitフックのインストール（初回のみ）
uv run --frozen pre-commit install

# pre-commitの手動実行
uv run --frozen pre-commit run --all-files

# pre-commitの自動更新（定期的に実行推奨）
uv run --frozen pre-commit autoupdate
```

## アーキテクチャに関する注意

- **インメモリストレージ**: データベースなし - データはアプリケーション実行時のみ保持
- **テストコンテキスト**: インストールなしで`product_api`をインポートするために`tests/context.py`を使用
- **プロジェクト構造**: メインAPIコードは`src/product_api/`、テストは`tests/`（srcレイアウト採用）
- **エラーハンドリング**: 適切なバリデーションとHTTPステータスコードの実装
- **認証なし**: このワークショップの範囲外

## 開発フロー

### Issue駆動開発

このプロジェクトはissue駆動開発を採用しています：

1. **要件確認**: docs/requirements.mdなどで要件を確認
2. **タスク分解**: 15-30分で完了可能なタスクに分解
3. **Issue登録**: GitHub CLIを使用して各タスクをissueとして登録
4. **開発**: 各issueごとにブランチを作成し、TDDアプローチで実装
5. **PR作成**: テストの通過を確認後、PRを作成してレビューを依頼

#### ブランチ命名規則

- `feature/task-{issue-number}-{brief-description}`
- 例: `feature/task-1-project-setup`

#### GitHub CLI使用例

```bash
# Issueの作成（改行には$'...'構文を使用）
gh issue create -t "タイトル" -b $'## 概要\n実装の説明\n\n## 実装内容\n- [ ] 項目1\n- [ ] 項目2'

# PRの作成
gh pr create \
  --title "feat: 機能名" \
  --body $'## 概要\n変更内容の説明\n\n## 関連Issue\nFixes #1'
```

## TDD（テスト駆動開発）実践ガイド

### t-wada方式TDDの黄金律

**実装コードを書く前に、必ず失敗するテストを書く。**

この原則は絶対に破ってはいけません。

### TDDサイクル

#### 1. Red（失敗するテストを書く）

- 失敗するテストを**1つだけ**書く
- テストの意図が明確になるよう命名する
- 実行して失敗を確認（エラーメッセージを読む）

#### 2. Green（テストを通す）

- テストを通すための**最小限**のコードを書く
- 実装戦略：
  - **仮実装（Fake It）**: まず固定値を返す
  - **三角測量（Triangulation）**: 複数のテストから一般化
  - **明白な実装（Obvious Implementation）**: 自信がある場合のみ

#### 3. Refactor（リファクタリング）

- すべてのテストが通る状態を保つ（グリーンキープ）
- 重複を除去し、設計を改善
- 小さなステップで進める

### TDD実践の重要原則

1. **TODOリストの活用**
   - 実装すべきテストケースをリストとして管理
   - 1つずつ順番に実装

2. **1テスト1アサーション**
   - アサーションルーレットを避ける
   - 複数の検証が必要なら、テストを分割

3. **段階的な実装**
   - 仮実装 → 三角測量 → 一般化の順で進める

### 実践例

```python
# ステップ1: Red（失敗するテスト）
def test_create_product_returns_201():
    response = client.post("/items", json={"name": "商品", "price": 100})
    assert response.status_code == 201  # 失敗

# ステップ2: Green（最小限の実装）
@app.post("/items", status_code=201)
def create_item():
    return {}  # 仮実装

# ステップ3: 次のテストを追加してリファクタリング
```

### コミット戦略

- Red: `git commit -m "test: add test for ..."`
- Green: `git commit -m "feat: implement minimal ..."`  
- Refactor: `git commit -m "refactor: extract ..."`

### 重要原則：pre-commit後のテスト確認

**絶対的ルール**: pre-commitフックが自動修正を行った場合、必ずテストを再実行してグリーンを確認する

```bash
# pre-commitが自動修正した場合の正しい流れ
git commit -m "..."  # pre-commitが動作、自動修正が発生
# → pre-commitに組み込まれたpytestが自動実行される
# → 全テストがグリーンであることを確認してからコミット完了
```

これにより、t-wada方式TDDの「グリーンキープ」原則を維持できます。

## 開発ガイドライン

### コード品質要件

- **型ヒント**: すべてのコードで必須
- **ドキュメント**: パブリックAPIで必須
- **関数設計**: 小さく、焦点を絞った関数
- **行長制限**: 最大100文字
- **テスト**: 新機能とバグ修正で必須
- **Markdown**: ファイル編集後は常にmarkdownlintでチェックし、エラーがゼロであることを確認

### パッケージ管理ルール

- **必須**: uvのみを使用、pipは禁止
- **基本操作**: まず`uv sync`でプロジェクトを同期（pyproject.tomlから自動認識）
- **新規追加**: 必要な場合のみ`uv add package` / `uv add --dev package`
- **ツール実行**: `uv run tool`
- **禁止**: `uv pip install`、既存の依存関係の重複追加、`@latest`構文

**重要**: pyproject.tomlで依存関係がすでに定義されている場合は、
`uv add`で重複追加せず、`uv sync`のみを使用してください

### テスト要件

- **フレームワーク**: `uv run --frozen pytest`
- **非同期テスト**: anyioを使用、asyncioは禁止
- **カバレッジ**: エッジケースとエラーケース
- **TDD実践**: t-wada氏推奨の方式を厳格に適用（詳細は下記TDDセクション参照）

## 技術的制約

- Python 3.12以上が必要
- ローカルPython環境での開発（Docker不要）
- 外部データベースなし
- 認証/認可なし
- 更新/削除操作なし（作成と読み取りのみ）
- 自動生成ドキュメントを備えたREST API用のFastAPI
- Cloud RunへのデプロイはMCP経由で自動化

## Gitコミットガイドライン

- ユーザーレポートに基づくバグ修正や機能の場合：

  ```bash
  git commit --trailer "Reported-by:<name>"
  ```

- GitHub Issueに関連する場合：

  ```bash
  git commit --trailer "Github-Issue:#<number>"
  ```

- **禁止**: `co-authored-by`やツール使用への言及は絶対に避ける

## プルリクエスト

- 変更の詳細な説明を含める
- 解決される問題とその解決方法に焦点を当てる
- **禁止**: `co-authored-by`やツール使用への言及は絶対に避ける

## エラー解決

### CI失敗の解決順序

1. フォーマットの修正
2. 型エラーの修正
3. Lintエラーの修正

### 一般的な問題

- **行長制限**: 括弧で文字列を分割、複数行の関数呼び出し、インポートの分割
- **型エラー**: Optional、型の絞り込み、関数シグネチャの確認をチェック
- **pytest実行失敗**: まず`uv sync`を実行、既存の依存関係を重複させない
- **カバレッジ測定失敗**: pyproject.tomlですでに設定済み、追加の設定ファイルは不要
- **Pytest**: anyio pytestマークが見つからない場合は、`PYTEST_DISABLE_PLUGIN_AUTOLOAD=""`を追加

### ベストプラクティス

- コミット前にgit statusをチェック
- 型チェック前にフォーマッタを実行
- Markdownファイル編集後は常にmarkdownlintを実行
- 変更を最小限に保つ
- 既存のパターンに従う
- パブリックAPIは常にドキュメント化

## 重要な指示のリマインダー

求められたことだけを行い、それ以上でも以下でもありません。

目標を達成するために絶対に必要でない限り、決してファイルを作成しないでください。

常に新しいファイルを作成するよりも既存のファイルを編集することを優先してください。

決して積極的にドキュメントファイル（*.md）やREADMEファイルを作成しないでください。
ユーザーから明示的に要求された場合にのみドキュメントファイルを作成してください。

## important-instruction-reminders

求められたことだけを行い、それ以上でも以下でもありません。
目標を達成するために絶対に必要でない限り、決してファイルを作成しないでください。
常に新しいファイルを作成するよりも既存のファイルを編集することを優先してください。
決して積極的にドキュメントファイル（*.md）やREADMEファイルを作成しないでください。
ユーザーから明示的に要求された場合にのみドキュメントファイルを作成してください。
