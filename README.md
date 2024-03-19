# Zapata AI challenge! 
Translate text to SQL query to then execute against a postgres database, and dockerize it all.

# Running the app

**IMPORTANT:** After cloning the repo, you must first obtain my defog api key. Create a file called `.env.defog` in the root directory of this repo, and put this line in it:
```
DEFOG_API_KEY = XXX
```
Where XXX is my api key. I will send the key in the email in which I send the link to this repo. I'm on defog's free tier, which means 1000 free requests per month.

Then just do a `docker compose up --build` in the root of the project. This should build the images from the Dockerfiles, then start the postgres and fastapi containers from these images (the postgres database automatically populates with the csv file on startup).

To stop everything just go Ctrl+C, and to destroy everything just go `docker compose down`.

## Testing the app
The fastapi container is listening on port 8000, which is also mapped to port 8000 on the host. The `query-test.py` script can be used to contact localhost:8000 and send questions. 

First, `pip install requests tabulate` if you don't already have these modules. Do so in a virtual environment if you'd like.

Then just go `python query-test.py`.

### Example Questions

The data is 2014-2023 data on TSLA stock, so some questions you could ask include:
 - What was the stock's opening price Jan 2 2014?
 - What's the average stock price for the first 10 days of 2020?
 - What are the 5 dates when the stock had the highest close price?

## Manually viewing the database

The fastapi container hits up the postgres container through a docker network, but the postgres container also maps the port it's listening on to host port 5400. 

So you can connect to localhost:5400 using a tool like pgAdmin to view the database directly (e.g., to check that what the app is returning is correct). Default user is `postgres` with password `supersecret`.

# Notes

### "Sorry :( Our server is at capacity right now"

"Sorry :( Our server is at capacity right now and we are unable to process your query. Please try again in a few minutes?" is an error I've gotten from defog; I use their api to translate text to sql, and sometimes they just can't. 

I guess in that case just try again in a few minutes like they say? :(

### Contact
You can contact me at `bryan.yan@mail.utoronto.ca` if you have questions about the app or need the defog api key.