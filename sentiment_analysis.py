import httpx

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": "Bearer test-dummy-key-for-integration",
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "Analyze the sentiment of the text as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": "0xtc qpNrn2ar2g\n Da1Wyubl\nuojZFI4S hIRx6SDmrWBcV j"
        }
    ]
}
response = httpx.post(url, headers=headers, json=data)
print(response.json())