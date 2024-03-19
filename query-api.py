import os

from fastapi import FastAPI
from pydantic import BaseModel
from defog import Defog
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class Question(BaseModel):
  question: str

@app.post("/query")
async def query(reqJSON: Question):
  question = reqJSON.question

  defog = Defog(
    api_key = os.getenv("DEFOG_API_KEY"),
    db_type = "postgres",
    db_creds = {
      "host": os.getenv("DB_HOST"),
      "port": os.getenv("DB_PORT"), 
      "database": os.getenv("DB_NAME"),
      "user": "postgres",
      "password": os.getenv("DB_PASSWORD")
    }
  )

  results = defog.run_query(question)
  if (results["ran_successfully"]):
    return {
      "columns": results["columns"],
      "data": results["data"],
      "ran_successfully": True
    }
  else:
    if (results["error_message"]): # if defog sends back an eerror message (not when SQL isn't right, but when they can't even generate the SQL for some reason)
      return results
    else:
      return {
        "ran_successfully": False,
        "attempted_query": results["query_generated"],
        "full_info": results
      }
