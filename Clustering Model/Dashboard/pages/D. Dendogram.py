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

# Creating Dendogram from Dataset
import scipy.cluster.hierarchy as shc

st.title('Dendogram')
plt.figure(figsize=(10, 7))
plt.title("Customer Dendograms")
dend = shc.dendrogram(shc.linkage(data, method='ward' ))

st.pyplot(plt)


plt.figure(figsize=(10,7))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.hlines(y=190,xmin=0,xmax=2000,lw=3,linestyles='--')
plt.text(x=900,y=220,s='Horizontal line crossing 5 vertical lines',fontsize=20)
#plt.grid(True)
dendrogram = shc.dendrogram(shc.linkage(data, method = 'ward'))
st.pyplot(plt)