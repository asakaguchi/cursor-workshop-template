"""商品管理UI - Streamlitアプリケーション.

商品管理APIと連携する Web インターフェース。
商品の登録と表示機能を提供。
"""

import os
from datetime import datetime
from typing import Dict, List, Optional

import httpx
import streamlit as st
from pydantic import BaseModel, ValidationError


class Product(BaseModel):
    """商品データモデル."""

    id: int
    name: str
    price: float
    created_at: datetime


class APIClient:
    """商品管理API クライアント."""

    def __init__(self, base_url: str) -> None:
        """初期化."""
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client()

    def create_product(self, name: str, price: float) -> Product | None:
        """商品を作成."""
        try:
            response = self.client.post(
                f"{self.base_url}/items",
                json={"name": name, "price": price},
            )
            response.raise_for_status()
            return Product(**response.json())
        except (httpx.HTTPError, ValidationError) as e:
            st.error(f"商品作成エラー: {e}")
            return None

    def get_product(self, product_id: int) -> Product | None:
        """商品を取得."""
        try:
            response = self.client.get(f"{self.base_url}/items/{product_id}")
            response.raise_for_status()
            return Product(**response.json())
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            st.error(f"商品取得エラー: {e}")
            return None
        except (httpx.HTTPError, ValidationError) as e:
            st.error(f"商品取得エラー: {e}")
            return None

    def health_check(self) -> bool:
        """APIの稼働状況を確認."""
        try:
            response = self.client.get(f"{self.base_url}/health")
            response.raise_for_status()
            return response.json().get("status") == "healthy"
        except httpx.HTTPError:
            return False


def main() -> None:
    """メインアプリケーション."""
    st.set_page_config(
        page_title="商品管理システム",
        page_icon="📦",
        layout="wide",
    )

    st.title("📦 商品管理システム")
    st.markdown("商品の登録と表示ができるシステムです")

    # API URL の設定
    api_url = os.getenv("API_URL", "http://localhost:8080")
    api_client = APIClient(api_url)

    # API接続確認
    col1, col2 = st.columns([3, 1])
    with col1:
        st.text(f"API URL: {api_url}")
    with col2:
        if api_client.health_check():
            st.success("✅ API接続OK")
        else:
            st.error("❌ API接続エラー")
            st.stop()

    # タブで機能を分離
    tab1, tab2 = st.tabs(["商品登録", "商品検索"])

    with tab1:
        st.header("新しい商品を登録")

        with st.form("product_form"):
            name = st.text_input("商品名", placeholder="例: りんご")
            price = st.number_input("価格", min_value=0.01, step=0.01, format="%.2f")
            submitted = st.form_submit_button("登録")

            if submitted:
                if name.strip():
                    product = api_client.create_product(name.strip(), price)
                    if product:
                        st.success(f"✅ 商品「{product.name}」を登録しました！（ID: {product.id}）")
                        st.json({
                            "id": product.id,
                            "name": product.name,
                            "price": product.price,
                            "created_at": product.created_at.isoformat(),
                        })
                else:
                    st.error("商品名を入力してください")

    with tab2:
        st.header("商品を検索")

        product_id = st.number_input("商品ID", min_value=1, step=1)

        if st.button("検索"):
            product = api_client.get_product(product_id)
            if product:
                st.success("✅ 商品が見つかりました")

                # 商品情報を表示
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("商品名", product.name)
                with col2:
                    st.metric("価格", f"¥{product.price:,.2f}")
                with col3:
                    st.metric("登録日時", product.created_at.strftime("%Y-%m-%d %H:%M"))

                # 詳細情報
                with st.expander("詳細情報"):
                    st.json({
                        "id": product.id,
                        "name": product.name,
                        "price": product.price,
                        "created_at": product.created_at.isoformat(),
                    })
            else:
                st.error("❌ 指定されたIDの商品は見つかりませんでした")

    # フッター
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Cursor Workshop - 商品管理システム</div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
