# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response

# Write directly to the app
st.title(":lollipop: Customize Your Smoothie :lollipop:")
st.write(
    """Choose your fruits you want in your custom smoothie.
    """)

name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on Smoothie is:", name_on_order)
cnx = st. connection ("snowflake")
session = cnx.session()
my_dataframe = session. table ("smoothies.public.fruit_options").select (col ('FRUIT_NAME'))
#my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
#st. dataframe(data-my_dataframe, use_container_width)

# Convert the Snowpark Dataframe to a Pandas Dataframe so we
can use the LOC function
pd_df=my_dataframe. to_pandas()
st. dataframe (pd_df)
st. stop()

ingredients_list = st.multiselect('Choose up to 5 ingredients:',my_dataframe, max_selections=5)

if ingredients_list:
    ingredients_string = ''
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ''
    #st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string +"""','"""+name_on_order+ """')"""
    # st.write(my_insert_stmt) 
    # st.stop()|
    time_to_insert = st.button( 'Submit Order')
    




