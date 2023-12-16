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



st.title('Corelation Matrix ')
## Finding Correlation between features
# Compute the correlation matridata
corr_matridata = customer_data.corr()

# Create a correlation heatmap
plt.figure(figsize=(5, 5))
sns.heatmap(corr_matridata, annot=True, cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()

st.pyplot(plt)

st.markdown(
    '''
    From above correlation graph will conclude that ,`CustomerID`,`Gender` these features of no use for our model.
     So we will drop these features from our dataset.
    '''
)