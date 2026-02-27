"""RunPod Serverless Handler — KURE-v1 임베딩 서버.

요청: {"input": {"text": "검색할 텍스트"}}
응답: {"embedding": [0.123, -0.456, ...]}  (1024차원)
"""
import runpod
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("nlpai-lab/KURE-v1")
print("[handler] KURE-v1 모델 로드 완료")


def handler(event):
    text = event["input"].get("text", "")
    if not text:
        return {"error": "text is required"}

    embedding = model.encode([text])[0].tolist()
    return {"embedding": embedding}


runpod.serverless.start({"handler": handler})
