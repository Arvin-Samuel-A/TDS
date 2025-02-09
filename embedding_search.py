from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import httpx
import math

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["*"]
)

class DocsQuery(BaseModel):
    docs: list[str]
    query: str

def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2)

async def get_embedding(text: str):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDA2MjdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.HMgfVdF9lKsRIlAt8uzqkUEisiurF9xhKJ9g8Tn7luA",
        "Content-Type": "application/json"
    }
    data = {
        "model": "text-embedding-3-small",
        "input": text
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        response_data = response.json()
        return response_data["data"][0]["embedding"]

@app.post("/similarity")
async def similarity_endpoint(payload: DocsQuery):
    query_embedding = await get_embedding(payload.query)
    
    # Compute document embeddings and similarities
    scores = []
    for i, doc in enumerate(payload.docs):
        doc_embedding = await get_embedding(doc)
        sim = cosine_similarity(query_embedding, doc_embedding)
        scores.append((doc, sim))
    
    # Sort by similarity descending
    scores.sort(key=lambda x: x[1], reverse=True)
    
    # Return top three matches
    top_matches = [doc for doc, _ in scores[:3]]
    return {"matches": top_matches}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)