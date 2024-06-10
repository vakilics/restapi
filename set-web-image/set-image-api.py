import requests
import streamlit as st

key = "jzwZBW8gbh34MdFJ064JHdp5ng7EX7t3aHTrPnWd"
url = "https://api.nasa.gov/planetary/apod?" \
       f"api_key={key}"

response1 = requests.get(url)
data = response1.json()

title = data ["title"]
image_url = data["url"]
explanation = data["explanation"]
image_fliepath = "img.png"
response2 = requests.get(image_url)
with open(image_fliepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_url)
st.write(explanation)




