import streamlit as st
import pandas as pd 
import  numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from app import *
import time


#loading data
data = load_data()
#Loading Processed data
customer_data = processed_data(data)
data = customer_data.iloc[:, 1:4].values


st.title("Building Model(Clustering)")

# Clustering Method Input
option = st.selectbox(
    'Select your clustering method',
    ('single', 'complete', 'average','ward'))

st.write('You selected:', option)

# Number of Cluster input
cluster_no = st.slider('Select number of cluster you want to create ', 1, 8)
st.write("Cluster to be created ", cluster_no)

# Loading spinner added
with st.spinner('Wait for it...'):
    time.sleep(1)
    st.success('Model Build Successfully !')

# Training Model
from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=cluster_no, affinity='euclidean', linkage= option )
# Output 
prediction = cluster.fit_predict(data)


plt.plot()
sns.scatterplot(y = "Spending Score (1-100)" , x= "Annual Income (k$)" , data = customer_data , hue = prediction , palette="rainbow")
st.pyplot(plt)


st.markdown(" For best Results select clustering Method `Ward` & Number of Cluster `5` ")