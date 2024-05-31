import requests
from send_email import tomail
api_key = "cf8258fee30549c383985b1fde5f45c3"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-04-30&sortBy=publishedAt&apiKey="
       "cf8258fee30549c383985b1fde5f45c3")
requests = requests.get(url)
#content = requests.text
content = requests.json()

body = ""
for article in content["articles"]:
    title = article["title"] if article["title"] is not None else ""
    description = article["description"] if article["description"] is not None else ""
    body = body + title + "\n" + description + "\n\n"

body = body.encode("utf-8")

#print(body)
tomail(message=body)