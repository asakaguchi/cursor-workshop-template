# 商品管理API

FastAPIベースの商品管理REST API

## 機能

- ヘルスチェック (`GET /health`)
- 商品作成 (`POST /items`)
- 商品取得 (`GET /items/{id}`)

## 起動方法

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

## API仕様

Swagger UI: http://localhost:8080/docs

## Cloud Run デプロイ

このディレクトリ全体をCloud Runにデプロイ可能です。