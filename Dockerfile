FROM python:3.11-alpine

# Install build tools, compilers, and libraries
RUN apk add --no-cache \
    build-base \
    gcc \
    g++ \
    python3-dev \
    libffi-dev \
    openssl-dev \
    musl-dev \
    linux-headers

# Set the working directory
WORKDIR /code

# Copy requirements and install dependencies
COPY ./requirements.txt /code/requirements.txt

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application files
COPY ./app /code/app

ENV PYTHONPATH="/code:${PYTHONPATH}"

# Run the application
CMD ["python", "app/main.py"]
