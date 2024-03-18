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
      "host": "localhost",
      "port": 5432, 
      "database": "test_db",
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
    return {
      "ran_successfully": False,
      "attempted_query": results["query_generated"],
      "full_info": results
    }
