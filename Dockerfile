FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu && \
    pip install --no-cache-dir runpod sentence-transformers

COPY handler.py /app/handler.py

CMD ["python", "-u", "/app/handler.py"]
