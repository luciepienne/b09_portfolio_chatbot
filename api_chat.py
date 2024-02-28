import json
import requests
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
from bs4 import BeautifulSoup

from key import my_key

# Check if my_key is empty or missing
if not my_key or my_key == "":
    print(
        "Your key is not filled or missing. Please provide a key compatible with EdenAI."
    )
    exit(1)

headers = {"Authorization": f"Bearer {my_key}"}

# Fetch the HTML content from the URL
response = requests.get("http://localhost:8001")
soup = BeautifulSoup(response.content, "html.parser")

app = FastAPI()

origins = ["http://localhost", "http://localhost:8001"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)
# for test only
# @app.get("/test/{prompt}", description="etst!")
# def test(prompt):
#       return "yo"


@app.post("/{prompt}")
async def chat(prompt):
    data = soup.get_text().strip()
    provider = "meta"
    url = "https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": provider,
        "text": "",
        "chatbot_global_action": f"Act as an assistant of Lucie with this : {data}, limit your answer to 20 words",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": "",
    }
    payload["text"] = prompt
    response = requests.post(url, json=payload, headers=headers)
    print("your question has been sent to Lucie's assistant")
    result = json.loads(response.text)
    if response.status_code != 200:
        print(f"Failed to fetch response. Status code: {response.status_code}")
        raise HTTPException(
            status_code=500, detail="Failed to fetch response from chatbot"
        )
    rp = result[provider]
    print(rp)
    answer = rp["generated_text"]
    return answer


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
