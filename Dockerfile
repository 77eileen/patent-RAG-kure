FROM runpod/base:0.6.2-cuda12.2.0

RUN pip install --no-cache-dir runpod sentence-transformers torch

COPY handler.py /handler.py

CMD ["python", "/handler.py"]
