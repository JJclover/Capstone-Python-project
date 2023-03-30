




SQLALCHEMY_SILENCE_UBER_WARNING = 1
SQLALCHEMY_WARN_20 = 0
import datetime
from sqlalchemy import create_engine, engine, text
import pandas as pd
import numpy as np


import os
import sqlalchemy
SQLALCHEMY_SILENCE_UBER_WARNING = 1
SQLALCHEMY_WARN_20 = 0
import datetime
from sqlalchemy import create_engine, engine, text
import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


import requests



# Load configuration from the YAML file
# Load App Engine configuration from the app.yaml file
with open('app.yaml') as app_file:
    app_config = yaml.load(app_file, Loader=SafeLoader)

# Load custom configuration from the config.yaml file
with open('config.yaml') as config_file:
    custom_config = yaml.load(config_file, Loader=SafeLoader)

image_url = "https://upload.wikimedia.org/wikipedia/commons/5/53/H%26M-Logo.svg"
st.image(image_url, width=200)

# Create the authenticator object
authenticator = stauth.Authenticate(
    custom_config['credentials'],
    custom_config['cookie']['name'],
    custom_config['cookie']['key'],
    custom_config['cookie']['expiry_days'],
    custom_config['preauthorized']
)

# Render the login widget
name, authentication_status, username = authenticator.login('Login', 'main')

# # Check authentication status and display content accordingly



if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    





    def load_data(response_json):
        try:
            data =pd.json_normalize(response_json, "result")
        except Exception as e:
            print(e)
        return data





    st.sidebar.write("FILTERS")

    # Call the API to get the initial data
    
    response_transactions = requests.get('https://api-dot-directed-racer-376415.oa.r.appspot.com/api/v1/transactions',
                                        params={'min_price': 0.0, 'max_price': 1.0},
                                        headers={"Authorization": "Bearer ilovecapstone"})
    transactions_data = response_transactions.json()['result']
    transactions_df = pd.DataFrame(transactions_data)

    # This is the code to make a filter for the different channel IDs
    channelID_lst = transactions_df["sales_channel_id"].unique().tolist()

    channelID_filtered_lst = st.sidebar.multiselect(
        label="sales_channel_id",
        options=channelID_lst,
        default=channelID_lst,
        key="multiselect_channel"
    )

    st.sidebar.write('sales_channel_id selected:', channelID_filtered_lst)

    # This is the code to create a filter for the price
    min_price = transactions_df["price"].min()
    max_price = transactions_df["price"].max()

    price_filtered_lst = st.sidebar.slider(
        'Select a range of price',
        float(min_price), float(max_price), (float(min_price), float(max_price)), 0.0001)

    st.sidebar.write('Price range selected:', price_filtered_lst)

    # Call the API with the selected filters
   
    response_filtered_transactions = requests.get('https://api-dot-directed-racer-376415.oa.r.appspot.com/api/v1/transactions',
                                                params={'sales_channel_id': channelID_filtered_lst,
                                                        'min_price': price_filtered_lst[0],
                                                        'max_price': price_filtered_lst[1]},
                                                        headers={"Authorization": "Bearer ilovecapstone"})

    filtered_transactions_data = response_filtered_transactions.json()['result']
    filtered_transactions_df = pd.DataFrame(filtered_transactions_data)

    # Display the filtered data
    st.subheader("Here you find the table with the information regarding the transactions")
    st.write(filtered_transactions_df)





   
    
    response_customers = requests.get('https://api-dot-directed-racer-376415.oa.r.appspot.com/api/v1/customers',headers={"Authorization": "Bearer ilovecapstone"})
    customers_data = response_customers.json()['result']
    customers_df = pd.DataFrame(customers_data)

    # This is the code to create a filter for the age
    age_lst = customers_df["age"].unique().tolist()

    age_filtered_lst = st.sidebar.slider(
        'Select a range of ages',
        min(age_lst), max(age_lst), (20, 80))

    st.sidebar.write('age range selected:', age_filtered_lst)

    # This is the code to create a filter for the club member status
    club_member_status_lst = customers_df["club_member_status"].unique().tolist()

    club_member_status_filtered_lst = st.sidebar.multiselect(
        label="club_member_status",
        options=club_member_status_lst,
        default=club_member_status_lst,
        key="multiselect_status"
    )

    st.sidebar.write('member status selected:', club_member_status_filtered_lst)

    # Call the API with the selected filters
    
    response_filtered_customers = requests.get('https://api-dot-directed-racer-376415.oa.r.appspot.com/api/v1/customers',
                                        params={'min_age': age_filtered_lst[0],
                                                'max_age': age_filtered_lst[1],
                                                'club_member_status': club_member_status_filtered_lst},
                                                headers={"Authorization": "Bearer ilovecapstone"})

    filtered_customers_data = response_filtered_customers.json()['result']
    filtered_customers_df = pd.DataFrame(filtered_customers_data)

    # Display the filtered data
    st.subheader("Here you find the table with the information regarding the customers")
    st.dataframe(filtered_customers_df)




 
    
    response_articles = requests.get('https://api-dot-directed-racer-376415.oa.r.appspot.com/api/v1/articles',headers={"Authorization": "Bearer ilovecapstone"})
    articles_data = response_articles.json()['result']
    articles_df = pd.DataFrame(articles_data)

    # This is the code to create a filter for the product_group_name
    productgroup_lst = articles_df["product_group_name"].unique().tolist()

    productgroup_filtered_lst = st.sidebar.multiselect(
        label="product_group_name",
        options=productgroup_lst,
        default=None,
        key="multiselect_productgroups"
    )

    st.sidebar.write('Product_group selected:', productgroup_filtered_lst)

    # This is the code to create a filter for the colour_group_name
    color_lst = articles_df["colour_group_name"].unique().tolist()

    color_filtered_lst = st.sidebar.multiselect(
        label="color",
        options=color_lst,
        default=None,
        key="multiselect_colorgroups"
    )

    st.sidebar.write('Color_group selected:', color_filtered_lst)

   
    
    response_filtered_articles = requests.get('https://api-dot-directed-racer-376415.oa.r.appspot.com/api/v1/articles',
                                            params={'product_group_name': productgroup_filtered_lst,
                                                    'colour_group_name': color_filtered_lst},
                                                    headers={"Authorization": "Bearer ilovecapstone"})

    filtered_articles_data = response_filtered_articles.json()['result']
    filtered_articles_df = pd.DataFrame(filtered_articles_data)

    # Display the filtered data
    st.subheader("Here you find the table with the information regarding the articles")
    st.dataframe(filtered_articles_df)





    st.title('Some KPIs')
    # Calculate KPI values
    # Could also do # of custmers with transactions table 
    num_customers = filtered_customers_df["customer_id"].nunique()
    num_articels = filtered_articles_df["article_id"].nunique()
    avg_age = np.mean(filtered_customers_df["age"])
    num_transactions = filtered_transactions_df["index"].nunique()
    avg_price= np.mean(filtered_transactions_df["price"])
    num_active_accounts = filtered_customers_df[filtered_customers_df['club_member_status'] == 'ACTIVE']['customer_id'].nunique()


    # Create KPIs
    kpi1, kpi2, kpi3, = st.columns(3)
    kpi4,kpi5,kpi6 = st.columns(3)

    kpi1.metric(
        label="Number of different customers",
        value=num_customers,
        delta=num_customers,
    )

    kpi2.metric(
        label="number of different articles",
        value=num_articels,
        delta=num_articels,
    )

    kpi3.metric(
        label="Average age",
        value=round(avg_age, 2),
        delta=-10 + avg_age,
    )

    kpi4.metric(
        label="number of different transactions",
        value=num_transactions,
        delta=num_transactions,
    )

    kpi5.metric(
        label="Average price",
        value=round(avg_price, 2),
        delta=-10 + avg_price,
    )

    kpi6.metric(
        label="Number of active accounts",
        value=num_active_accounts,
        delta=num_active_accounts,
    )





    st.title('Some Graphs')
    # st.bar_chart(customer_df.groupby(["age"]).count())   --> This does age barchart for variables

    st.write("in the following histograms you can see the age distribution")
    st.bar_chart(filtered_customers_df.groupby(["age"])["customer_id"].count())

    st.write("in the following histograms you can see the club member status distribution")
    st.bar_chart(filtered_customers_df.groupby(["club_member_status"])["customer_id"].count())


    st.write("in the following histograms you can see the sales channels distribution")
    st.bar_chart(filtered_transactions_df.groupby(["sales_channel_id"])["customer_id"].count())


    st.write("in the following histograms you can see the product groups distribution")
    st.bar_chart(filtered_articles_df.groupby(["product_group_name"])["article_id"].count())

    st.write("in the following histograms you can see the sections distribution")
    st.bar_chart(filtered_articles_df.groupby(["section_name"])["article_id"].count())






    






elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

