import requests
import json

query = input("Which type of news you want to see? ")
from_date = input("Enter the news date (YYYY-MM-DD): ")
to_date = input("Enter the news date (YYYY-MM-DD): ")

url = f"https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&sortBy=publishedAt&apiKey=ad1337ae1a9840629ce5a231aadcd120"

r = requests.get(url)
news = json.loads(r.text)

if "articles" in news:
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print()
        print("-------------------------------------------------------------------------------------------")
        print()
else:
    print("Sorry, no articles were found for your query.")
