import streamlit as st
import requests


api_key = "YOUR API KEY"  # here set your NASA api key
request_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"  # url to apod

# Gets the request data as dictionary
response1 = requests.get(request_url)  # we send request to api
data = response1.json()  # here we store the data, title, explanation, url to image...

title = data['title']  # we extract the data we want and store them
image_url = data['url']
explanation = data['explanation']

image_filepath = "img.png"  # setting image path (img.png will appear in project folder)
response2 = requests.get(image_url)  # from requesting url to the image of the day we get another response

with open(image_filepath, "wb") as file:  # open it as img.png in web browser
    file.write(response2.content)  # from image url response we take content, we download the image


st.title(title)  # here goes three lines that make our streamlit web interface
st.image(image_filepath)
st.write(explanation)

st.write("From portfolio:")
link = "https://s1fam-portfolio-home-at8i55.streamlit.app"
st.markdown(link, unsafe_allow_html=True)
