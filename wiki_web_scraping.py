import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/outline")
def get_outline(country: str):
    # Build Wikipedia URL
    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    
    # Fetch page
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Wikipedia page not found")
    
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract headings (h1 to h6)
    headings = soup.select("h1, h2, h3, h4, h5, h6")

    # Generate Markdown outline
    markdown_outline = "## Contents\n\n"
    for heading in headings:
        level = int(heading.name[-1])  # e.g., 'h2' -> level 2
        marker = "#" * level
        text = heading.get_text(strip=True)
        markdown_outline += f"{marker} {text}\n\n"

    return {"outline": markdown_outline}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)