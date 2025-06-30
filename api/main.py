"""商品管理API - FastAPIアプリケーション.

シンプルな商品管理機能を提供するREST API。
インメモリストレージを使用し、永続化は行わない。
"""

from datetime import datetime
from typing import Dict, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    """商品作成リクエスト."""

    name: str = Field(..., min_length=1, description="商品名（1文字以上）")
    price: float = Field(..., gt=0, description="価格（0より大きい数値）")


class Product(BaseModel):
    """商品レスポンス."""

    id: int = Field(..., description="商品ID")
    name: str = Field(..., description="商品名")
    price: float = Field(..., description="価格")
    created_at: datetime = Field(..., description="作成日時")


class HealthResponse(BaseModel):
    """ヘルスチェックレスポンス."""

    status: str = Field(..., description="ステータス")


app = FastAPI(
    title="商品管理API",
    description="シンプルな商品管理機能を提供するREST API",
    version="0.1.0",
)

# インメモリストレージ
products: dict[int, Product] = {}
next_id = 1


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """APIの稼働状況を確認."""
    return HealthResponse(status="healthy")


@app.post("/items", response_model=Product, status_code=201)
async def create_product(product_data: ProductCreate) -> Product:
    """新しい商品を作成."""
    global next_id

    product = Product(
        id=next_id,
        name=product_data.name,
        price=product_data.price,
        created_at=datetime.now(),
    )

    products[next_id] = product
    next_id += 1

    return product


@app.get("/items/{product_id}", response_model=Product)
async def get_product(product_id: int) -> Product:
    """指定されたIDの商品を取得."""
    if product_id not in products:
        raise HTTPException(status_code=404, detail="商品が見つかりません")

    return products[product_id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
