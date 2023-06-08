import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header ('Breakfast Favourites')
streamlit.text('Omega 3 and blueberry oatmeal')
streamlit.text('Kale, spinach & rocket smoothie')
streamlit.text('Hard Boiled free-range egg')
streamlit.text('Avocado toast')

streamlit.header('Build your own smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
