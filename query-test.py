import requests
import json

url = "http://localhost:8000/query"  

question = {
  "question": "What are the 5 dates when the stock had highest close price?"
}

reqJSON = json.dumps(question)

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=reqJSON, headers=headers)

if response.status_code == 200:
  print(response.json())
else:
  print(f"Error: {response.status_code} - {response.text}")
