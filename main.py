import requests

api_key = "cf8258fee30549c383985b1fde5f45c3"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-04-30&sortBy=publishedAt&apiKey="
       "cf8258fee30549c383985b1fde5f45c3")
requests = requests.get(url)
#content = requests.text
#print(type(content))
content = requests.json()
#print(content["articles"])

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
