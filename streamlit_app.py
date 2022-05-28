import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('fruityvice fruit advice!')
f=streamlit.text_input('what fruit would you like to get the information','apple')
streamlit.write('the user entered',f);
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+f)
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)



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

 
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into fruit_load_list values('jackfruit')")
      return "thanks for adding"+new_fruit

add_my_fruit=streamlit.text_input('what fruit wouldnu like to add?')
                  
if streamlit.button('add a fruit to list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function=insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)   
   
if streamlit.button('Get fruit List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows=get_fruit_load_list();
   my_cnx.close();
   streamlit.dataframe(my_data_rows)  
   
 
                     




               

