import streamlit
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Apple'])
f=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(f)

streamlit.header('fruityvice advice')
import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


import snowflake.connector
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cnx=my_cnx.cursor()
my_cnx.execute("SELECT CURRENT_USER(),CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row=my_cnx.fetchone();
streamlit.text("Hello from snowflake: ")
streamlit.text(my_data_row)

               

