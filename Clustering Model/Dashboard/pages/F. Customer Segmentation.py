import streamlit as st
import pandas as pd 
import  numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from app import *
import time
from model import csv_to_model , pie_chart , cluster_analysis


st.title('Shopping Mall Customer Segmentation')
st.markdown('''
- Upload your csv file
- Make sure that your csv file have these columns in it `( Age , Annual Income (k$) ,Spending Score (1-100) )`
- That all for now :smile:
''')



uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    # Read the uploaded file
    customer_data = pd.read_csv(uploaded_file)
    #calling csv_to_model
    data = csv_to_model(customer_data)
    # calling pie_chart 
    img = pie_chart(data)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(img)
    st.title('Cluster Analysis')
    df = csv_to_model(customer_data)
    analysis_data = cluster_analysis(df)
    st.write(analysis_data)


df = pd.DataFrame(analysis_data)
st.table(df)









