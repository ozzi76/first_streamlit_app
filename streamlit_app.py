import pandas as pd
import streamlit

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.header('My Fruits')

fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado','Strawberries'])

if len(my_fruit_list.loc[fruits_selected]) > 0:
  streamlit.dataframe(my_fruit_list.loc[fruits_selected])
else:
  streamlit.dataframe(my_fruit_list)
