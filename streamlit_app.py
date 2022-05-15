
import streamlit

streamlit.title('My Mom\'s New Health Diner')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.title('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Lets put a pick list here so that they can pick any fruit they want from fruit list
fruit_selected = streamlit.multiselect ("Pick Some Fruits : ", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

#Display the table on the page
streamlit.dataframe(fruit_to_show)

#New Section to Display fruityvice API response
#streamlit.header('Fruityvice FRuit ADvice\!')

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

#take the json version of the response and normalize it
#fruityvice_narmalized = pandas.json_narmalize(fruityvice_response.json())
#output it as table
#streamlit.dataframe(fruityvice_narmalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
