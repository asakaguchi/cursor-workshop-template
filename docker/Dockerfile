ARG BUILDER_IMAGE=ubuntu:24.04
ARG RUNNER_IMAGE=ubuntu:24.04

FROM ${BUILDER_IMAGE} AS builder

RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        git

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

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
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        sudo \
        gosu && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Configure environment
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /workspace

# Copy virtual environment from builder
COPY --from=builder /app/.venv /workspace/.venv

# Copy source code
COPY . .

# Copy entrypoint script
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Install project in development mode (if main.py exists)
RUN --mount=type=cache,target=/root/.cache/uv \
    if [ -f "src/product_api/main.py" ]; then \
        uv sync; \
    else \
        uv sync --no-install-project; \
    fi

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]