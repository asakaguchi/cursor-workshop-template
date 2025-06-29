# MCP (Model Context Protocol) 設定ガイド

## 概要

このプロジェクトでは以下のMCPサーバーが設定されています：

- **Cloud Run MCP**: Google Cloud Runへのデプロイ自動化
- **Context7 MCP**: 最新ライブラリドキュメントの取得
- **Playwright MCP**: ブラウザ自動化とWebテスト（新規追加）

## Playwright MCP について

### 特徴

- **高速軽量**: スクリーンショットではなくアクセシビリティツリーを使用
- **LLM対応**: 構造化データで動作（ビジョンモデル不要）
- **決定論的**: 曖昧さのない正確な操作
- **多ブラウザ対応**: Chromium、Firefox、WebKit

### 利用可能な機能

1. **ブラウザ操作**
   - ページナビゲーション
   - クリック、入力、選択操作
   - スクリーンショット撮影

2. **テスト支援**
   - アクセシビリティスナップショット
   - ネットワークリクエスト監視
   - PDF保存

3. **タブ管理**
   - 複数タブの操作
   - タブ間の切り替え

## 設定ファイル

### 基本設定（.mcp.json）

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

### 高度な設定（.mcp-playwright-config.json）

プロジェクトルートに配置された設定ファイルでは以下をカスタマイズ可能：

- **ブラウザ設定**: Chromium、Firefox、WebKitから選択
- **実行モード**: ヘッドレス/ヘッド付き
- **ビューポート**: 画面サイズの指定
- **プロファイル**: 永続化または分離モード

## 使用例

AIとの対話で以下のようにPlaywright機能を活用できます：

```text
ブラウザでGoogleを開いて、「Cursor AI」を検索してください
```

```text
現在のページのスクリーンショットを撮影してください
```

```text
フォームに商品名「テストアイテム」と価格「100」を入力して送信してください
```

## セキュリティ注意事項

- **プロファイル保存**: デフォルトでブラウザプロファイルが保存されます
- **ネットワーク制限**: 必要に応じて allowed-origins/blocked-origins を設定
- **分離モード**: テスト時は isolated: true を推奨

## トラブルシューティング

### Node.js要件
- Node.js 18以上が必要
- `node --version` で確認

### 権限エラー
- macOS: セキュリティ設定でブラウザ起動を許可
- Windows: ウイルス対策ソフトの除外設定

### ブラウザインストール
```bash
npx playwright install chromium
```

## 参考リンク

- [Microsoft Playwright MCP 公式](https://github.com/microsoft/playwright-mcp)
- [Playwright ドキュメント](https://playwright.dev/)
- [MCP 仕様](https://modelcontextprotocol.io/)