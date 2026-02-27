import runpod
from sentence_transformers import SentenceTransformer

print("KURE-v1 모델 로딩 중...")
model = SentenceTransformer("nlpai-lab/KURE-v1")
print("KURE-v1 모델 로딩 완료!")

def handler(event):
    text = event["input"]["text"]
    embedding = model.encode([text])[0].tolist()
    return {"embedding": embedding}

runpod.serverless.start({"handler": handler})
