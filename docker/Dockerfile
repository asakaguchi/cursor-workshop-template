ARG BUILDER_IMAGE=ubuntu:24.04
ARG RUNNER_IMAGE=ubuntu:24.04

FROM ${BUILDER_IMAGE} AS builder

ENV DEBIAN_FRONTEND=noninteractive \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git

# Install uv
RUN --mount=type=cache,target=/root/.cache/uv \
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy dependency files
COPY pyproject.toml ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-editable

FROM ${RUNNER_IMAGE} AS production

# Install runtime dependencies
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git \
        sudo \
        gosu \
        zsh \
        nodejs \
        npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Install markdownlint-cli globally
RUN npm install -g markdownlint-cli

# Add uv to PATH
ENV PATH="/root/.local/bin:/app/.venv/bin:$PATH"

# Configure environment
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /app/.venv /app/.venv

# Copy source code
COPY . .

# Copy entrypoint script
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Install project in development mode (if main.py exists)
RUN --mount=type=cache,target=/root/.cache/uv \
    if [ -f "src/product_api/main.py" ]; then \
        uv sync --extra dev; \
    else \
        uv sync --no-install-project --extra dev; \
    fi

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]