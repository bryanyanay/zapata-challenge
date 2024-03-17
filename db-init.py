import os
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()

def createDB(dbName):
  try:
    conn = psycopg2.connect(
      dbname="postgres", 
      user="postgres", 
      password=os.getenv("DB_PASSWORD"), 
      host="localhost",
      port="5432"
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE {dbName}")
    print(f"Created database: {dbName}")
  
  except OperationalError as e:
    print(f"Error: {e}")
  finally:
    cur.close()
    conn.close()

createDB("test_db")