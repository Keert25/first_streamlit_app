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
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('please select a fruit to get information')
  else:
    
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

 

#streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("list of fruits:")
streamlit.text(my_data_row)
#streamlit.write('tahnks for adding',add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")



               

