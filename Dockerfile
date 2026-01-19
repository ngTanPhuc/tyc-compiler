# Multi-stage build for TyC Compiler
FROM python:3.12-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies for ANTLR
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run setup to generate ANTLR files
RUN python3 run.py setup

# Final stage
FROM python:3.12-slim

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

# Copy installed dependencies from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application from builder
COPY --from=builder /app /app

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app:$PATH"

# Default command
CMD ["python3", "run.py", "help"]
