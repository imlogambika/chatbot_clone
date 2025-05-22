import requests

def search_query(query):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": "5f385e13f38ac6f79f218084b7fca8446f08d5a0",  #  API Key
        "Content-Type": "application/json"
    }
    payload = {
        "q": query
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

results = search_query("Artificial Intelligence in Education")
for result in results.get("organic", []):
    print(result['title'], "-", result['link'])
