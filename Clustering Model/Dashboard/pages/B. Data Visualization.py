import streamlit as st
import pandas as pd 
import  numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from app import *


#loading data
data = load_data()
#Loading Processed data
customer_data = processed_data(data)


# distribution plots


#sns.distplot(customer_data['Age'])
plt.figure(figsize = (20, 8))
plotnumber = 1

for col in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:
    if plotnumber <= 3:
        adata = plt.subplot(1, 3, plotnumber)
        sns.distplot(customer_data[col])
        
    plotnumber += 1
    
plt.tight_layout()
plt.show()

st.title('Distribution Graph')
st.pyplot(plt)

st.markdown("All Graph is almost have a bell curve which denotes there no skewness and have no need to perform Normalisation , Standardisation ")