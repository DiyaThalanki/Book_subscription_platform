# # backend/Dockerfile

# FROM python:3.11-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add test dependencies now (pytest etc.)
RUN pip install pytest
RUN pip install pytest-mock

COPY . .

# Clear bad caches (important when developing)
RUN rm -rf __pycache__ .pytest_cache

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



