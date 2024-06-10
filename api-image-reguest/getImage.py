import requests

url = "https://en.wikipedia.org/wiki/Flower#/media/File:Flower_poster_2.jpg"

response = requests.get(url)
print(response.content)

with open("image.jpg", "wb") as file:
    file.write(response.content)

