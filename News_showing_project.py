import requests
import json

query = input("Which type of news you want to see? ")
date = input("Enter the news date (YYYY-MM-DD): ")

url = f"https://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey=ad1337ae1a9840629ce5a231aadcd120"

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
