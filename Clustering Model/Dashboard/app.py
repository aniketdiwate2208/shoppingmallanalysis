import streamlit as st
import pandas as pd 
import  numpy as np 
from sklearn.preprocessing import OneHotEncoder



st.title("Shopping Mall Analysis :tea:")
st.markdown('Identifying patterns in the data collected at a Shopping Mall based on customer spend score & demographics using Hierarchical Clustering')

st.markdown('''

## Content
- You are owing a supermarket mall and through membership cards , you have some basic data about your customers like Customer ID, age, gender, annual income and spending score.
Spending Score is something you assign to the customer based on your defined parameters like customer behavior and purchasing data.

- You own the mall and want to understand the customers like who can be easily converge [Target Customers] so that the sense can be given to marketing team and plan the strategy accordingly

## 

''')



@st.cache_data
def load_data():
    customer_data = pd.read_csv('Mall_Customers.csv')
    return customer_data


def processed_data(customer_data):
    #One Hot Encoding 
    ohe = OneHotEncoder(drop='first',sparse=False,dtype=np.int32)
    data_new = ohe.fit_transform(customer_data[['Genre']])
    customer_data['Gender'] = data_new
    # Drop a single column
    customer_data = customer_data.drop('Genre', axis=1)


    return customer_data


