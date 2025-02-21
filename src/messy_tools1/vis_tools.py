import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def _import_file(file):
    """
    Imports the stated file 
    allows for the function and .py file to be run from any directory
    prints a message and the first 5 lines of the DataFrame
    returns data 
    """
    # finds and saves the path of the file which allows the package to be moved
    file_path = Path(__file__).parent 
    data = pd.read_csv(f'{file_path}/data/{file}')
    
    # displays and returns the data as a Pandas DataFrame
    print('Data loaded:')
    print(data.head(5))
    return data

def basic_stats(data: pd.Series):
    """
    Compute basic statistics on a single column of a dataframe 
    display an output 
    return mean_value & std_value
    """
    # Run basic stats 
    mean_value = data.mean() 
    std_value = data.std()
    
    # Display results with a clean output
    print(f"Mean of {data.columns}: {mean_value}")
    print(f"Standard deviation of {data.columns}: {std_value}")
    return mean_value, std_value

def display_graph(data: pd.DataFrame, dimensions: list, column_names: list):
    """
    Function that displays a scatter plot figure based on the inputs using matplotlib 
    dimensions : set figure size
    column_names : sets the columns that will be called for visualizations 
    data : the data frame the visualization is based on 
    """
    plt.figure(figsize=(dimensions[0],dimensions[1]))
    plt.scatter(data[column_names[0]], data[column_names[1]], c='blue', alpha=0.5)
    # Sets Labels for the figure 
    plt.title(f'Scatter plot of {column_names[0]} vs. {column_names[1]}')
    plt.xlabel(column_names[0])
    plt.ylabel(column_names[1])
    plt.show

