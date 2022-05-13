import streamlit
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruits_selected=streamlit.multiselect("pick some fruits",list(my_fruit_list.index),['Avocado','Apple'])
f=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(f)

