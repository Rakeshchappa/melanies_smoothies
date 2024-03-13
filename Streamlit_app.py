# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
# Write directly to the app
st.title(":cup_with_straw: Pending Smoothie Orders :cup_with_straw:")
st.write(
    """Choose the fruits you want in the custom smoothie!
    """
)



# #-- creating a drop down


# option = st.selectbox(
#     'What is your favourite fruit?',
#     ('Banana', 'Strawberries', 'Peaches'))

# st.write('Your favourite fruit is:', option)




name_on_order = st.text_input('NAme on Smoothie: ')
st.write('The name of your smoothie will be: ', name_on_order)


session = get_active_session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
# st.dataframe(data=my_dataframe, use_container_width=True)



edited_df = st.experimental_data_editor(my_dataframe)

Submitted=st.button('Submit')



if Submitted:
       st.success('Some one clicked the button', icon="👍")
    
       og_dataset = session.table("smoothies.public.orders")
       edited_dataset = session.create_dataframe(edited_df)
       try:
           og_dataset.merge(edited_dataset
                     , (og_dataset['order_uid'] == edited_dataset['order_uid'])
                     , [when_matched().update({'ORDER_FILLED': edited_dataset['ORDER_FILLED']})]
                    )

           st.success('Order(s) Updated!', icon="👍")
       except:
           st.write('Something went wrong')

else:
    st.success('There is no pending Ordes right now!', icon="👍")





# ingredients_list=st.multiselect(
#     'choose up to 5 ingredients:',
#     my_dataframe
# )


# # st.write(ingredients_list)
# # st.text(ingredients_list)

# # if ingredients_list:
#     # st.write(ingredients_list)
#     # st.text(ingredients_list)   
    


# if ingredients_list:
    
    
#     ingredients_string =''
#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen+' '
#     st.write(ingredients_string)


#     my_insert_stmt = """ insert into smoothies.public.orders(ingredients,NAME_ON_ORDER)
#             values ('""" + ingredients_string +"""','"""""+name_on_order+ """')"""

#     time_to_insert=st.button('Submit Order')
#     if time_to_insert:
#         session.sql(my_insert_stmt).collect()
        
#         st.success('Your Smoothie is ordered!', icon="✅")
cnx=st.connection("snowflake")
session=cnx.session()






