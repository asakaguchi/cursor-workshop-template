# CLAUDE.md

このファイルは、このリポジトリでコードを扱う際のClaude Code（claude.ai/code）向けのガイダンスを提供します。

**注意**: Cursorエディタを使用する場合は、`.cursor/rules/`ディレクトリの
ルールファイルも参照してください。特に以下が重要です：

- `python-structure.mdc`: モダンなPythonプロジェクト構造（srcレイアウト）
- `code-quality-enforcement.mdc`: コード品質・開発ガイドライン
- `development-workflow.mdc`: 開発フローとGitHub連携
- `pep8-enforcement.mdc`: Pythonコーディング規約

## 参考資料

このプロジェクトは以下の資料を参考にして構築されています：

- **記事**: [モダンなPython開発環境をDockerで構築する](https://zenn.dev/mjun0812/articles/0ae2325d40ed20)
- **テンプレート**: [mjun0812/python-project-template](https://github.com/mjun0812/python-project-template)
  - 特に [CLAUDE.md](https://github.com/mjun0812/python-project-template/blob/main/CLAUDE.md) の構成を参考

Docker設定、uv使用方法、プロジェクト構造など、多くの要素が上記資料に基づいています。

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
- **プロジェクト構造**: メインAPIコードは`src/product_api/`、テストは`tests/`（srcレイアウト採用）
- **エラーハンドリング**: 適切なバリデーションとHTTPステータスコードの実装
- **認証なし**: このワークショップのスコープ外

## 開発フロー

### Issue駆動開発

このプロジェクトでは Issue 駆動開発を採用しています：

1. **要件確認**: docs/requirements.md などの要件を確認
2. **タスク分解**: 要件を15-30分で完了可能なタスクに分解
3. **Issue登録**: GitHub CLI で各タスクを Issue として登録
4. **開発実施**: Issue ごとにブランチを作成してTDDアプローチで実装
5. **PR作成**: テスト通過確認後、PR作成してレビュー依頼

#### ブランチ名規則

- `feature/task-{issue番号}-{簡潔な説明}`
- 例: `feature/task-1-project-setup`

#### GitHub CLI使用例

```bash
# Issue作成（改行を含む場合は $'...' 構文を使用）
gh issue create -t "タイトル" -b $'## 概要\n実装内容の説明\n\n## 実装内容\n- [ ] 項目1\n- [ ] 項目2'

# PR作成
gh pr create \
  --title "feat: 機能名" \
  --body $'## 概要\n変更内容の説明\n\n## 関連Issue\nFixes #1'
```

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
- **基本操作**: まず `uv sync` でプロジェクト同期（pyproject.tomlから自動認識）
- **新規追加**: 必要な場合のみ `uv add package` / `uv add --dev package`
- **ツール実行**: `uv run tool`
- **禁止**: `uv pip install`、既存依存関係の重複追加、`@latest`構文

**重要**: pyproject.tomlに依存関係が既に定義されている場合は、
`uv add` で重複追加せず、`uv sync` のみを使用する

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
- **pytest実行失敗**: まず `uv sync` を実行、既存依存関係を重複追加しない
- **カバレッジ計測失敗**: pyproject.tomlに設定済み、追加設定ファイル不要
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

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
