# zapata-challenge
Zapata AI challenge! Translate text to SQL query to then execute against a postgres database, and dockerize it all.

# Notes

 - may want to use user that is limited to read (suggested by the model card)
 - must predownload the model when dockerizing it
 - may wanna rework the venv to not include everything we didn't use
 - had to separately install pandas for defog init
 - if we change the db we gotta rerun defog init i believe


rakeshkiriyath/gpt2Medium_text_to_sql
cssupport/t5-small-awesome-text-to-sql


Given a table with this schema:

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

Write a valid postgreSQL query to answer this question: What's the opening price of the stock on December 29 2023?

Below are sql tables schemas paired with instruction that describes a task. 
Using valid postgreSQL, write a response that appropriately completes the request for the provided tables. 
### Instruction: What's the opening price of the stock on December 29 2023?
### Database: test_db
### Input: 
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