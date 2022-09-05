
import streamlit
import requests

streamlit.title("Bio- Data");
streamlit.header("Name - Sumanth Dixit");
streamlit.text("I reside in India, age is 28 and I love snowflake");
   
streamlit.title('My moms new healthy diner');
streamlit.header(' Breakfast Menu ');
streamlit.text('🥣Omega 3 & Blueberry Oatmeal');
streamlit.text('🥗Kale, Spinach & Rocket Smoothie');
streamlit.text('🐔Hard-Boiled Free-Range Egg');
streamlit.text('🥑🍞Avocado Toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
