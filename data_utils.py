import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

def barplot_with_missing_values_columns(dataframe):

    #the amount of missing values per column
    missing_counts = dataframe.isnull().sum()
    #filtering away the columns that don't have missing values
    missing_counts = missing_counts[missing_counts > 0]

    #creating a dataframe for plotting
    missing_df = missing_counts.reset_index() #creates a normal index 
    missing_df.columns = ['Column', 'Count'] 

    plt.figure(figsize=(8,5))
    sns.barplot(x="Column", y= "Count", data= missing_df, palette='viridis')
    plt.title("Null values")
    plt.xticks(rotation=45, ha="right")
    plt.show()