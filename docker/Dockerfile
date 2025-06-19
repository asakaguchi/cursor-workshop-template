# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12
ARG UV_VERSION=0.5.23

# ========================================
# Base stage: Python環境の基本設定
# ========================================
FROM python:${PYTHON_VERSION}-slim AS base

# 環境変数の設定
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# 作業ディレクトリの設定
WORKDIR /workspace

# ========================================
# UV stage: uvのインストール
# ========================================
FROM base AS uv-installer

# uvのインストール（公式インストーラーを使用）
RUN --mount=type=cache,target=/root/.cache/pip \
    apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    curl -LsSf https://astral.sh/uv/${UV_VERSION}/install.sh | sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ========================================
# Dependencies stage: 依存関係のインストール
# ========================================
FROM base AS dependencies

# uvをコピー
COPY --from=uv-installer /root/.local/bin/uv /usr/local/bin/uv

# プロジェクトファイルをコピー（依存関係のみ）
COPY pyproject.toml uv.lock ./

# 依存関係のインストール（キャッシュマウントを使用）
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# ========================================
# Development stage: 開発環境
# ========================================
FROM dependencies AS development

# 開発用パッケージのインストール
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# 開発ツールのインストール
RUN --mount=type=cache,target=/root/.cache/pip \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        vim \
        less \
        procps \
        htop \
        net-tools \
        iputils-ping \
        dnsutils \
        build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Node.js のインストール（markdownlint-cli用）
RUN --mount=type=cache,target=/root/.cache \
    curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g markdownlint-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# pyrightのインストール
RUN npm install -g pyright

# ソースコードをコピー
COPY . .

# プロジェクトのインストール（開発モード）
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# FastAPI開発サーバー用ポート
EXPOSE 8000

# 開発サーバーの起動
CMD ["uv", "run", "uvicorn", "src.product_api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# ========================================
# Production stage: 本番環境（最小構成）
# ========================================
FROM dependencies AS production

# ソースコードをコピー
COPY src ./src

# プロジェクトのインストール（本番モード）
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# 非rootユーザーの作成と切り替え
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /workspace

USER appuser

# FastAPI本番サーバー用ポート
EXPOSE 8000

# ヘルスチェック
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD uv run python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# 本番サーバーの起動
CMD ["uv", "run", "uvicorn", "src.product_api.main:app", "--host", "0.0.0.0", "--port", "8000"]