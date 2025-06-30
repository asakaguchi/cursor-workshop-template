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

これはPythonとFastAPIを使用して**商品管理API**を構築するための
Cursorワークショップテンプレートです。
インメモリストレージを使用したシンプルなREST APIを実装します。

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
# FastAPIサーバーの起動（ルートディレクトリから）
uv run uvicorn api.main:app --reload

# または api/ ディレクトリから
cd api && uv run uvicorn main:app --reload

# Swagger UIへのアクセス: http://localhost:8080/docs
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
- **分離デプロイ構造**: APIは`api/`、UIは`ui/`に独立配置（Cloud Run対応）
- **テストコンテキスト**: 分離構造に対応した`tests/context.py`を使用
- **プロジェクト構造**: APIコードは`api/`、UIコードは`ui/`、テストは`tests/`
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

**絶対的ルール**: 以下の場合は必ず手動でテストを再実行してグリーンを確認する

1. pre-commitフックが自動修正を行った場合
2. pre-commitでエラーが発生して手動修正した場合

```bash
# ケース1: pre-commitが自動修正した場合
git commit -m "..."  # pre-commitが動作、自動修正が発生

# ケース2: pre-commitでエラーが発生した場合
git commit -m "..."  # pre-commitが失敗、エラーメッセージを表示
# → エラーを手動で修正

# いずれの場合も、以下を必ず実行：
uv run --frozen pytest  # 手動でテスト実行
# → 全テストがグリーンであることを確認してから再度コミット
git add .
git commit -m "..."  # 修正されたファイルでコミット
```

**重要**: AIは以下の場合に必ずpytestを手動実行してからコミットを完了すること：

- pre-commitが自動修正した場合
- pre-commitエラーで手動修正した場合
- コードを直接編集した場合

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

#### パッケージ管理緊急対応プロトコル（必須遵守）

**テストライブラリ不足エラーの場合：**

##### 手順1: 環境確認（必須）

```bash
pwd  # プロジェクトルートにいることを確認
cat pyproject.toml | grep -A 10 "dev"  # 既存依存関係を確認
```

##### 手順2: ルート環境への統一追加

```bash
# 絶対にapi/やui/ではなく、プロジェクトルートで実行
uv add --dev pytest httpx asgi-lifespan trio fastapi
uv sync
```

##### 手順3: 検証（必須）

```bash
uv run --frozen pytest tests/ --collect-only  # テスト収集確認
uv run --frozen pytest tests/api/ -v  # 実際のテスト実行
```

**絶対禁止事項:**

- ❌ 異なるディレクトリでの`uv add`後、別ディレクトリでのテスト実行
- ❌ `cd api && uv add` → `cd .. && pytest`のような環境混在
- ❌ エラー時の応急処置的なパッケージ追加

**AI開発者への強制指示:**

1. パッケージ追加前に必ず`pwd && ls pyproject.toml`で位置確認
2. 「なぜこのパッケージが必要か」を明確に説明
3. 「どこに追加すべきか」の判断根拠を提示
4. 環境不整合時は`uv sync`による再構築を最優先

#### 依存関係配置の明確なルール

```text
pyproject.toml (ルート) - テスト実行環境
├── dependencies: 共通ライブラリ
├── dev-dependencies: テスト・開発ツール全般
│   ├── pytest, httpx, asgi-lifespan, trio
│   ├── ruff, pyright, pre-commit
│   └── markdownlint-cli
│
api/pyproject.toml - 本番デプロイ用
├── dependencies: FastAPI実行に必要な最小限のみ
│   ├── fastapi>=0.100.0
│   ├── uvicorn[standard]>=0.23.0
│   └── pydantic>=2.0.0
│
ui/pyproject.toml - 本番デプロイ用
├── dependencies: Streamlit実行に必要な最小限のみ
│   ├── streamlit>=1.28.0
│   ├── httpx>=0.24.0
│   └── pydantic>=2.0.0
```

**実行コマンド統一（厳格に遵守）:**

- テスト: `uv run --frozen pytest` （常にプロジェクトルートから）
- API開発: `cd api && uv run uvicorn main:app --reload`
- UI開発: `cd ui && uv run streamlit run main.py`

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

### Cloud Run 分離デプロイ要件

**重要**: Cloud Run デプロイ時は、APIとUIを分離した独立構造で実装してください：

#### 必要な構造

```text
project/
├── api/
│   ├── pyproject.toml  # FastAPI専用（最小依存関係）
│   ├── main.py         # FastAPIアプリケーション
│   └── README.md
├── ui/
│   ├── pyproject.toml  # Streamlit専用（最小依存関係）
│   ├── main.py         # Streamlitアプリケーション
│   └── README.md
└── tests/              # テストファイル
```

#### 各pyproject.tomlの要件

**API用**: 依存関係は `fastapi>=0.100.0`, `uvicorn[standard]>=0.23.0`,
`pydantic>=2.0.0` のみ  
**UI用**: 依存関係は `streamlit>=1.28.0`, `httpx>=0.24.0`,
`pydantic>=2.0.0` のみ

#### デプロイ方法

各ディレクトリを `mcp__cloud-run__deploy_local_folder` で独立してデプロイ

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
