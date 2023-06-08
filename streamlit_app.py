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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Grapefruit', 'Kiwifruit'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
