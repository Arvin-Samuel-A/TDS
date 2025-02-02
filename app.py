from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []
with open("/mnt/c/Users/dell/OneDrive/Desktop/IITM/TDS/q-fastapi.csv", "r", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        students.append({"studentId": int(row["studentId"]), "class": row["class"]})

@app.get("/api")
def get_students(class_: list[str] = Query(None, alias="class")):
    if not class_:
        return {"students": students}
    return {"students": [s for s in students if s["class"] in class_]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)