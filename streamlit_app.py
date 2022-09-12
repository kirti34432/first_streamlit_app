import streamlit
streamlit.title('My parents new Healthy Dinner')
streamlit.header('breakfast Menu')
streamlit.text('🍒 Omega 3 & BlueBerry Oatmeal')
streamlit.text('☘ Kale,Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard Boiled Free Range Egg')
streamlit.text('🥪 Avacado toast')
streamlit.header('🍌🍍Build your own Smoothie 🥭🍓')



import pandas 
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
