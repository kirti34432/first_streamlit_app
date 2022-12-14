import streamlit
streamlit.title('My parents new Healthy Dinner')
streamlit.header('breakfast Menu')
streamlit.text('ð Omega 3 & BlueBerry Oatmeal')
streamlit.text('â Kale,Spinach & Rocket Smoothie')
streamlit.text('ð¥ Hard Boiled Free Range Egg')
streamlit.text('ð¥ª Avacado toast')
streamlit.header('ððBuild your own Smoothie ð¥­ð')



import pandas 
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)
