import json
import requests

headers = {"Authorization": "Bearer your_key"}

provider = "meta"
url = "https://api.edenai.run/v2/text/chat"
payload = {
        "providers": provider,
        "text": "",
        "chatbot_global_action": "Act as a developper and answer in less than 50 words",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": ""
    }

while True:
    prompt = input("Q: ")
    payload["text"] = prompt
    print("\n")

    if prompt in ["logout", "exit", "bye", "quit"]:
        break

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    rp = result[provider]
    answer = rp['generated_text']
    print(answer)
    # we add the previous question to history
    payload["previous_history"].append({'role':'user','message':prompt})
    # we add the previous answer to history
    payload["previous_history"].append({'role':'assistant','message': rp['generated_text']})

    print("\n")
    print(payload['previous_history'])
    print("\n")

