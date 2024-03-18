import os

from defog import Defog
from dotenv import load_dotenv

load_dotenv()

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

results = defog.run_query("What's the average stock for the first 10 days of 2020?")
print(results)
