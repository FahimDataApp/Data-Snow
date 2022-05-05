
import streamlit

streamlit.title('My Mom\'s New Health Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Lets put a pick list here so that they can pick any fruit they want from fruit list
streamlit.multiselect ("Pick Some Fruits : ", list(my_fruit_list.index))

#Display the table on the page
streamlit.dataframe(my_fruit_list)
