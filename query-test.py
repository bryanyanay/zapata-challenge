import json
import requests
from tabulate import tabulate

url = "http://localhost:8000/query"  

while True:
  print(">>> ENTER QUESTION (type 'quit' to exit): ", end="")
  userInput = input() 
  if userInput.strip().lower() == "quit":
    print("Exiting...")
    break

  question = {
    "question": userInput
  }
  reqJSON = json.dumps(question)
  headers = {"Content-Type": "application/json"}

  print(">>> ASKING: ", question["question"])
  response = requests.post(url, data=reqJSON, headers=headers)

  if response.status_code == 200:
    resJSON = response.json()
    if (resJSON["ran_successfully"]):
      print(">>> QUERY SUCCESSFUL")
      print(tabulate(resJSON["data"], headers=resJSON["columns"]))
    else:
      print(">>> QUERY NOT SUCCESSFUL")
      print(">>> ATTEMPTED QUERY:")
      print(resJSON["attempted_query"])
      print(">>> FULL INFO:")
      print(resJSON["full_info"])
  else:
    print(f"Error: {response.status_code} - {response.text}")
