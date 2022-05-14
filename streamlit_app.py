import pandas as pd
import streamlit
import snowflake.connector

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header('My Fruits')

fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado','Strawberries'])


streamlit.dataframe(my_fruit_list.loc[fruits_selected])

streamlit.header('Fruityvice Fruit Advice')

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice) 

import requests

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)

          
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list includes:")
streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')

streamlit.write('Thanks for adding ', add_my_fruit)

my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")
