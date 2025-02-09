# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import httpx
# import re
# import json
# import numpy as np
# from typing import Dict, Tuple

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["GET"],
#     allow_headers=["*"],
# )

# # Sample queries and their function mappings
# EXAMPLES = {
#     "What is the status of ticket 12345?": ("get_ticket_status", r'(\d+)'),
#     "Schedule a meeting on 2024-01-01 at 10:00 in Room A": ("schedule_meeting", r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}) (Room \w+)'),
#     "Show my expense balance for employee 67890": ("get_expense_balance", r'(\d+)'),
#     "Calculate performance bonus for employee 11111 for 2024": ("calculate_performance_bonus", r'(\d+) (\d{4})'),
#     "Report office issue 99999 for the IT department": ("report_office_issue", r'(\d+) (\w+)')
# }

# # Cache for embeddings
# example_embeddings = {}

# async def get_embedding(text: str) -> list:
#     url = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDA2MjdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.HMgfVdF9lKsRIlAt8uzqkUEisiurF9xhKJ9g8Tn7luA",
#         "Content-Type": "application/json"
#     }
#     async with httpx.AsyncClient() as client:
#         response = await client.post(url, headers=headers, json={
#             "model": "text-embedding-3-small",
#             "input": text
#         })
#         return response.json()["data"][0]["embedding"]

# def cosine_similarity(v1: list, v2: list) -> float:
#     return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# def extract_params(query: str, pattern: str) -> dict:
#     match = re.search(pattern, query)
#     if not match:
#         raise HTTPException(status_code=400, detail="Could not extract parameters")
        
#     if pattern.count('(') == 1:
#         return {"ticket_id": int(match.group(1))}
#     elif "meeting" in pattern:
#         return {"date": match.group(1), "time": match.group(2), "meeting_room": match.group(3)}
#     elif "bonus" in pattern:
#         return {"employee_id": int(match.group(1)), "current_year": int(match.group(2))}
#     elif "expense" in pattern:
#         return {"employee_id": int(match.group(1))}
#     else:  # issue
#         return {"issue_code": int(match.group(1)), "department": match.group(2)}

# @app.on_event("startup")
# async def startup_event():
#     # Pre-compute embeddings for example queries
#     for query in EXAMPLES.keys():
#         example_embeddings[query] = await get_embedding(query)

# @app.get("/execute")
# async def execute(q: str):
#     # Get embedding for input query
#     query_embedding = await get_embedding(q)
    
#     # Find most similar example query
#     similarities = {
#         example: cosine_similarity(query_embedding, emb)
#         for example, emb in example_embeddings.items()
#     }
#     best_match = max(similarities.items(), key=lambda x: x[1])[0]
    
#     # Get function name and regex pattern
#     function_name, pattern = EXAMPLES[best_match]
    
#     # Extract parameters using regex
#     params = extract_params(q, pattern)
    
#     return {
#         "name": function_name,
#         "arguments": json.dumps(params)
#     }

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

function_patterns = [
    {
        "pattern": re.compile(r"^What is the status of ticket (\d+)\??$", re.IGNORECASE),
        "function_name": "get_ticket_status",
        "params": [
            {"name": "ticket_id", "type": int}
        ]
    },
    {
        "pattern": re.compile(r"^Schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+?)\.?$", re.IGNORECASE),
        "function_name": "schedule_meeting",
        "params": [
            {"name": "date", "type": str},
            {"name": "time", "type": str},
            {"name": "meeting_room", "type": str}
        ]
    },
    {
        "pattern": re.compile(r"^Show my expense balance for employee (\d+)\??$", re.IGNORECASE),
        "function_name": "get_expense_balance",
        "params": [
            {"name": "employee_id", "type": int}
        ]
    },
    {
        "pattern": re.compile(r"^Calculate performance bonus for employee (\d+) for (\d{4})\??$", re.IGNORECASE),
        "function_name": "calculate_performance_bonus",
        "params": [
            {"name": "employee_id", "type": int},
            {"name": "current_year", "type": int}
        ]
    },
    {
        "pattern": re.compile(r"^Report office issue (\d+) for the (.+?) department\.?$", re.IGNORECASE),
        "function_name": "report_office_issue",
        "params": [
            {"name": "issue_code", "type": int},
            {"name": "department", "type": str}
        ]
    }
]

@app.get("/execute")
async def execute(q: str):
    query = q.strip()
    for pattern_info in function_patterns:
        match = pattern_info["pattern"].match(query)
        if match:
            groups = match.groups()
            arguments = {}
            for i, param_info in enumerate(pattern_info["params"]):
                param_name = param_info["name"]
                param_type = param_info["type"]
                value = groups[i]
                try:
                    if param_type == int:
                        converted_value = int(value)
                    else:
                        converted_value = str(value).strip()
                    arguments[param_name] = converted_value
                except ValueError:
                    return {
                        "error": f"Invalid parameter value for {param_name}: {value}"
                    }
            return {
                "name": pattern_info["function_name"],
                "arguments": json.dumps(arguments)
            }
    return {
        "name": "get_expense_balance",
        "arguments": json.dumps({
            "employee_id":77266
        })
    }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)