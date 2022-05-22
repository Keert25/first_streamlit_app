import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Apple'])
f=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(f)

streamlit.header('fruityvice advice')


def get_fruityvice_data(this_fruit_choice):
   fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    
   fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
streamlit.header('fruityvice advice')
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('please select a fruit to get information')
  else:
    
   back_from_function=get_fruityvice_data(fruit_choice)
   streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

 

#streamlit.stop()


streamlit.header("the fruit load list conatins:")
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from fruit_load_list")
      return my_cur.fetchall()

if streamlit.button('get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows=get_fruit_load_list()
   streamlit.dataframe(my_data_rows)                  
                     




               

