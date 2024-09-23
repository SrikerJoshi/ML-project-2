import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from langchain.llms import GoogleGemini
import os

# Initialize the Google Gemini LLM
llm = GoogleGemini(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))

def get_recipe(dish_name):
    # Interact with Google Gemini LLM to fetch Indian cuisine recipes
    prompt = f"Please provide a detailed recipe for {dish_name}. Be a helpful assistant."
    response = llm.generate(prompt)
    return response['text']

def get_youtube_link(dish_name):
    # Use Google Gemini LLM to search YouTube for relevant video links
    prompt = f"Find a YouTube video link for the recipe of {dish_name}."
    response = llm.generate(prompt)
    return response['text']

def get_images(dish_name):
    # Fetch images of the dishes using Google search
    search_url = f"https://www.googleapis.com/customsearch/v1?q={dish_name}&searchType=image&key={os.getenv('GOOGLE_API_KEY')}&cx={os.getenv('SEARCH_ENGINE_ID')}"
    response = requests.get(search_url).json()
    image_urls = [item['link'] for item in response['items'][:5]]
    images = [Image.open(BytesIO(requests.get(url).content)) for url in image_urls]
    return images

st.title("Indian Cuisine Chatbot")
st.write("Learn how to cook delicious Indian food with detailed recipes, images, and YouTube video links!")

dish_name = st.text_input("Enter the name of the dish you want to cook:")

if dish_name:
    recipe = get_recipe(dish_name)
    youtube_link = get_youtube_link(dish_name)
    images = get_images(dish_name)

    st.subheader("Recipe")
    st.write(recipe)

    st.subheader("Images")
    for image in images:
        st.image(image, caption=dish_name)

    st.subheader("YouTube Video")
    st.write(f"[Watch on YouTube]({youtube_link})")
