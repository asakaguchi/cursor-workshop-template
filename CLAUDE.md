# CLAUDE.md

このファイルは、このリポジトリでコードを扱う際のClaude Code（claude.ai/code）向けのガイダンスを提供します。

**注意**: Cursorエディタを使用する場合は、`.cursor/rules/`ディレクトリの
ルールファイルも参照してください。特に以下が重要です：

- `code-quality-enforcement.mdc`: コード品質・開発ガイドライン
- `development-workflow.mdc`: 開発フローとGitHub連携
- `pep8-enforcement.mdc`: Pythonコーディング規約

## プロジェクト概要

これはPythonとFastAPIを使用して**商品管理API**を構築するための
Cursorワークショップテンプレートです。インメモリストレージを使用した
商品管理のシンプルなREST APIを実装します。

## 主要要件

APIは以下を実装する必要があります：

- 商品作成（POST /items）
- 商品取得（GET /items/{id}）
- ヘルスチェック（GET /health）
- pytestを使用したTDDアプローチ
- 自動Swagger UI生成機能付きのFastAPIフレームワーク

### 商品データ構造

- id: Integer（自動生成）
- name: String（必須、1文字以上）
- price: Float（必須、0より大きい）
- created_at: Datetime（自動設定）

## 開発コマンド

### パッケージ管理

**重要**: 必ずuvを使用し、pipは使用しない

```bash
# 依存関係のインストール（禁止: uv pip install）
uv add fastapi uvicorn pytest

# 開発モードでプロジェクトをインストール
uv pip install -e .
```

### アプリケーションの実行

```bash
# FastAPIサーバーの起動
uvicorn product_api.main:app --reload

# Swagger UIにアクセス: http://localhost:8000/docs
```

### テスト

```bash
# 全テストの実行
uv run --frozen pytest

# 特定のテストファイルの実行
uv run --frozen pytest tests/test_filename.py

# 詳細出力でのテスト実行
uv run --frozen pytest -v

# anyioプラグイン問題がある場合
PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest
```

### コード品質チェック

```bash
# コードフォーマット
uv run --frozen ruff format .

# Lintチェック
uv run --frozen ruff check .

# Lint修正
uv run --frozen ruff check . --fix

# 型チェック
uv run --frozen pyright

# Markdownファイルのチェック（必須）
markdownlint *.md
```

## アーキテクチャ メモ

- **インメモリストレージ**: データベースなし - データはアプリケーション実行中のみ保持
- **テストコンテキスト**: インストールなしで`product_api`をインポートするために`tests/context.py`を使用
- **プロジェクト構造**: メインAPIコードは`product_api/`、テストは`tests/`
- **エラーハンドリング**: 適切なバリデーションとHTTPステータスコードの実装
- **認証なし**: このワークショップのスコープ外

## 開発ガイドライン

### コード品質要件

- **型ヒント**: すべてのコードに必須
- **ドキュメント**: パブリックAPIには必須
- **関数設計**: 小さく焦点を絞った関数
- **行長制限**: 最大88文字
- **テスト**: 新機能とバグ修正にはテスト必須
- **Markdown**: ファイル編集後は必ずmarkdownlintでチェックしエラーゼロにする

### パッケージ管理ルール

- **必須**: uvのみ使用、pipは禁止
- **インストール**: `uv add package`
- **実行**: `uv run tool`
- **禁止**: `uv pip install`、`@latest`構文

### テスト要件

- **フレームワーク**: `uv run --frozen pytest`
- **非同期テスト**: anyio使用、asyncio禁止
- **カバレッジ**: エッジケースとエラーケース

## 技術的制約

- Python 3.12以上が必要
- 外部データベースなし
- 認証・認可なし
- 更新・削除操作なし（作成と読み取りのみ）
- 自動生成ドキュメント付きのFastAPI for REST API

## Git コミットガイドライン

- バグ修正や機能追加がユーザーレポートに基づく場合：

  ```bash
  git commit --trailer "Reported-by:<name>"
  ```

- GitHub issueに関連する場合：

  ```bash
  git commit --trailer "Github-Issue:#<number>"
  ```

- **禁止**: `co-authored-by`やツール使用の言及は絶対に避ける

## プルリクエスト

- 変更内容の詳細な説明を記載
- 解決する問題とその解決方法に焦点を当てる
- **禁止**: `co-authored-by`やツール使用の言及は絶対に避ける

## エラー解決

### CI失敗時の対処順序

1. フォーマット修正
2. 型エラー修正
3. Lintエラー修正

### よくある問題

- **行長制限**: 文字列は括弧で分割、関数呼び出しは複数行、インポートは分割
- **型エラー**: Optionalのチェック、型の絞り込み、関数シグネチャの確認
- **Pytest**: anyio pytest markが見つからない場合は `PYTEST_DISABLE_PLUGIN_AUTOLOAD=""` を追加

### ベストプラクティス

- コミット前にgit statusを確認
- 型チェック前にフォーマッターを実行
- Markdownファイル編集後は必ずmarkdownlintを実行
- 変更は最小限に
- 既存パターンに従う
- パブリックAPIには必ずドキュメント

## 重要な指示リマインダー

Do what has been asked; nothing more, nothing less.
（求められたことを実行する。それ以上でも以下でもない。）

NEVER create files unless they're absolutely necessary for achieving your goal.
（目標達成に絶対に必要でない限り、ファイルは作成しない。）

ALWAYS prefer editing an existing file to creating a new one.
（新しいファイル作成より既存ファイル編集を常に優先する。）

NEVER proactively create documentation files (*.md) or README files.
Only create documentation files if explicitly requested by the User.
（ユーザーから明示的に要求されない限り、ドキュメントファイル（*.md）や
READMEファイルは積極的に作成しない。）
