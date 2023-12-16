import pickle
import numpy as np
import pandas as pd
import pickle
import sklearn
import seaborn as sns
from flask_cors import CORS
import csv
import matplotlib.pyplot as plt 


#Importing Files 
clustering = pickle.load(open('model.pkl','rb'))
X = pickle.load(open('data.pkl','rb'))

def predict_function(age,income,score ):
    """
    Predicts model output

    Parameters:
    age (int): The first number.
    income (int): The second number.
    score (int): The second number.
    """
    labels = {
    0: "Standard - middle income and middle spenders",
    1: "Careful - high income but low spenders",
    2: "Target group - middle-to-high income and high spenders (should be targeted by the mall)",
    3: "Careless - low income but high spenders (should be avoided because of possible credit risk)",
    4: "Sensible - low income and low spenders"
    }
    
    # Predict a single value
    new_data_point = np.array([[age, income ,score]])  # The new data point to predict
    
    # Concatenate new data point with existing data
    augmented_data = np.concatenate((X, new_data_point))
    
    # Refit the clustering algorithm
    clustering.fit(augmented_data)
    
    # Get the cluster labels
    cluster_labels = clustering.labels_
    
    # Retrieve the predicted cluster for the new data point
    predicted_cluster = cluster_labels[-1]

    prediction = {
    'Cluster': int(predicted_cluster),
    'labels' : labels[int(predicted_cluster)]  
    }

    return prediction


def csv_to_model(customer_data):
    """
    Takes Inpute as csv and trains clustering model with hierarchical clustering

    Parameters:
    customer_data (file )  it should be csv file

    Return:
    df : final preprocessed data + prediction  = dataframe

    """

    #Applying One Hot Encoding on Genre Column
    from sklearn.preprocessing import OneHotEncoder
    ohe = OneHotEncoder(drop='first',sparse=False,dtype=np.int32)
    data_new = ohe.fit_transform(customer_data[['Genre']])

    customer_data['Gender'] = data_new
    # Drop a single column
    customer_data = customer_data.drop('Genre', axis=1)

    #final Data 
    data = customer_data.iloc[:, 1:4].values

    #Building Model 
    from sklearn.cluster import AgglomerativeClustering
    cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward' ,)
    cluster.fit(data)

    # Output 
    prediction = cluster.fit_predict(data)

    #final Output dataframe 
    columns = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    df = pd.DataFrame(data , columns=columns)
    df['Cluster_Id'] = prediction
    return df



def pie_chart(df):
    """
    Takes Inpute as pandas dataframe  

    Parameters:
    df (pandas dataframe )  

    Return:
    Pie chart : pie_chart.png

    """



    # Printing Count of Values in Each cluster 
    df['Cluster_Id'].value_counts()
    values_in_cluster = []
    for i in df['Cluster_Id'].value_counts():
        values_in_cluster.append(i)
    
    # print(values_in_cluster)
    # Disable warning messages from Matplotlib

    plt.figure(figsize=(10,8))

    # Calculate the count or proportion of data points in each cluster
    # cluster_counts = [83, 39, 35 ,23 ,20]  # Example cluster counts
    cluster_counts = values_in_cluster #passing list here from above
    
    # Labels for the pie chart
    labels = ['Cluster 0' , 'Cluster 1', 'Cluster 2' , 'Cluster 3' , 'Cluster 4']
    labels2 = ['Cluster 0: "Standard - middle income and middle spenders' , 'Cluster 1: Careful - high income but low spenders', 'Cluster 2: Target group - middle-to-high income and high spenders (should be targeted by the mall)' , 'Cluster 3: Careless - low income but high spenders (should be avoided because of possible credit risk) ' , 'Cluster 4: Sensible - low income and low spenders']
    
    
    # Specify colors for each slice
    colors = ['#ADD8E6', '#90EE90', '#FFB6C1' ,'#FFFFE0' , '#E6E6FA']
    
    # Create the pie chart
    plt.pie(cluster_counts, labels=labels, colors=colors, autopct='%1.1f%%', )
    
    # Add a title
    plt.title('Cluster Distribution')
    # Add a legend
    plt.legend(labels2, loc='best')
    #figure Size
    
    
    # Display the pie chart
    img = plt.show()
    
    # sAVING fIGURE
    
    return img


def cluster_analysis(df):

    """
    Takes Inpute as pandas dataframe  

    Parameters:
    df (pandas dataframe )  

    Return:
    Pie chart : pie_chart.png

    """

    df[['Age', 'Annual Income (k$)','Spending Score (1-100)','Cluster_Id']].groupby('Cluster_Id').mean()
    # Grouping Data into seperate clusters
    group_0= df[df['Cluster_Id']==0]
    group_1= df[df['Cluster_Id']==1]
    group_2= df[df['Cluster_Id']==2]
    group_3= df[df['Cluster_Id']==3]
    group_4= df[df['Cluster_Id']==4]


    Analysis_data = {
    'cluster 0' : {
        'Average Age' : round(group_0.mean()['Age']),
        'Average Annual Income(K$)': round(group_0.mean()['Annual Income (k$)']),
        'Spending Score (1-100)': round(group_0.mean()['Spending Score (1-100)']),
        'Annual Income Range K$':{
            'Minimum Annual Income (K$)' : round(group_0.min()['Annual Income (k$)']),
            'Maximum Annual Income (K$)' : round(group_0.max()['Annual Income (k$)']),
            }, 
        'Cluster Spending Score' : {
            'Minimum Spending Score' : round(group_0.min()['Spending Score (1-100)']),
            'Maximum Spending Score' : round(group_0.max()['Spending Score (1-100)']),
        }

        },
    'cluster 1' : {
        'Average Age' : round(group_1.mean()['Age']),
        'Average Annual Income(K$)': round(group_1.mean()['Annual Income (k$)']),
        'Spending Score (1-100)': round(group_1.mean()['Spending Score (1-100)']),
        'Annual Income Range K$':{
            'Minimum Annual Income (K$)' : round(group_1.min()['Annual Income (k$)']),
            'Maximum Annual Income (K$)' : round(group_1.max()['Annual Income (k$)']),
            }, 
        'Cluster Spending Score' : {
            'Minimum Spending Score' : round(group_1.min()['Spending Score (1-100)']),
            'Maximum Spending Score' : round(group_1.max()['Spending Score (1-100)']),
        }
        },
    'cluster 2' : {
        'Average Age' : round(group_2.mean()['Age']),
        'Average Annual Income(K$)': round(group_2.mean()['Annual Income (k$)']),
        'Spending Score (1-100)': round(group_2.mean()['Spending Score (1-100)']),
        'Annual Income Range K$':{
            'Minimum Annual Income (K$)' : round(group_2.min()['Annual Income (k$)']),
            'Maximum Annual Income (K$)' : round(group_2.max()['Annual Income (k$)']),
            }, 
        'Cluster Spending Score' : {
            'Minimum Spending Score' : round(group_2.min()['Spending Score (1-100)']),
            'Maximum Spending Score' : round(group_2.max()['Spending Score (1-100)']),
        }
        },
    'cluster 3' : {
        'Average Age' : round(group_3.mean()['Age']),
        'Average Annual Income(K$)': round(group_3.mean()['Annual Income (k$)']),
        'Spending Score (1-100)': round(group_3.mean()['Spending Score (1-100)']),
        'Annual Income Range K$':{
            'Minimum Annual Income (K$)' : round(group_3.min()['Annual Income (k$)']),
            'Maximum Annual Income (K$)' : round(group_3.max()['Annual Income (k$)']),
            }, 
        'Cluster Spending Score' : {
            'Minimum Spending Score' : round(group_3.min()['Spending Score (1-100)']),
            'Maximum Spending Score' : round(group_3.max()['Spending Score (1-100)']),
        }
        },
    'cluster 4' : {
        'Average Age' : round(group_4.mean()['Age']),
        'Average Annual Income(K$)': round(group_4.mean()['Annual Income (k$)']),
        'Spending Score (1-100)': round(group_4.mean()['Spending Score (1-100)']),
        'Annual Income Range K$':{
            'Minimum Annual Income (K$)' : round(group_4.min()['Annual Income (k$)']),
            'Maximum Annual Income (K$)' : round(group_4.max()['Annual Income (k$)']),
            }, 
        'Cluster Spending Score' : {
            'Minimum Spending Score' : round(group_4.min()['Spending Score (1-100)']),
            'Maximum Spending Score' : round(group_4.max()['Spending Score (1-100)']),
        }
        },
}
    return Analysis_data