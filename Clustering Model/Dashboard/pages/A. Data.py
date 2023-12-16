import streamlit as st
import pandas as pd 
import  numpy as np 
from app import load_data



customer_data = load_data()
st.title('Shopping Mall dataset')
st.write(customer_data)

st.title('Description of datset')
st.write(customer_data.describe())