import os
import psycopg2
import csv
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

def createTable(dbName):
  try:
    conn = psycopg2.connect(
      dbname=dbName,
      user="postgres",
      password=os.getenv("DB_PASSWORD"),
      host="localhost",
      port="5432"
    )
    conn.autocommit = True

    cur = conn.cursor()

    cmd = """
      CREATE TABLE stock_data (
          date DATE PRIMARY KEY,
          open NUMERIC,
          high NUMERIC,
          low NUMERIC,
          close NUMERIC,
          volume BIGINT,
          rsi_7 NUMERIC,
          rsi_14 NUMERIC,
          cci_7 NUMERIC,
          cci_14 NUMERIC,
          sma_50 NUMERIC,
          ema_50 NUMERIC,
          sma_100 NUMERIC,
          ema_100 NUMERIC,
          macd NUMERIC,
          bollinger NUMERIC,
          TrueRange NUMERIC,
          atr_7 NUMERIC,
          atr_14 NUMERIC,
          next_day_close NUMERIC
      )
    """

    cur.execute(cmd)
    print("Table created successfully!")
  except OperationalError as e:
    print(f"Error: {e}")
  finally:
    cur.close()
    conn.close()

def loadCSVdata(dbName):
  try:
    conn = psycopg2.connect(
      dbname=dbName,
      user="postgres",
      password=os.getenv("DB_PASSWORD"),
      host="localhost",
      port="5432"
    )
    conn.autocommit = True

    cur = conn.cursor()
    csvFile = 'tsla_2014_2023.csv'

    # Open the CSV file and read data
    with open(csvFile, 'r') as file:
      reader = csv.reader(file)
      next(reader)  # Skip header row
      for row in reader:
        # Insert data into the table
        cur.execute("""
          INSERT INTO stock_data
          (date, open, high, low, close, volume, rsi_7, rsi_14, cci_7, cci_14, sma_50, ema_50, sma_100, ema_100, macd, bollinger, TrueRange, atr_7, atr_14, next_day_close)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, row)
    print("Data loaded successfully!")
  except OperationalError as e:
    print(f"Error: {e}")
  finally:
    cur.close()
    conn.close()

# createDB("test_db")
# createTable("test_db")
# loadCSVdata("test_db")