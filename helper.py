'''
This Module contains all the function required for cleaning and ploting of Data.
'''

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns



def plot_count_barchart(series):
    '''
    plot a barchart of frequencies of each element in pandas series 
    Args:
        series : pandas series
    '''
    sns.barplot(x=series.value_counts().index,y=series.value_counts().values)



# By looking at the id column in portfolio and profile DataFrame and 
# person column of transcript DataFrame

# These are the hash value associated with to each ids by coverting 
# it to int our further analysis would become easy

def map_id_to_int(arr, maped_values=None):
    '''
    Function to map hash id to a integer value.
    
    Args:
        data : Any 1d Iterable of hash ids.
        maped_values : Dictionary of maped integer associated with hash.
    Returns:
        maped_ids : Integer ID associated with each hash.
        viewed_ids : Dictionary of maped integer with each hash value.
    '''
    viewed_ids = {}
    maped_ids = []
    
    counter = 1
    
    if maped_values is None:
        for val in list(arr):
            if val in viewed_ids:
                maped_ids.append(viewed_ids[val])
            else :
                maped_ids.append(counter)
                viewed_ids[val] = counter
                counter += 1
                
    elif maped_values is not None:
        for val in list(arr):
            if val in maped_values:
                maped_ids.append(maped_values[val])
            elif pd.isnull(val):
                maped_ids.append(None)
            else :
                raise Exception(f"We Could not find value for id {val} in the given dictionary")
                
        viewed_ids = maped_values
        
    return maped_ids, viewed_ids




def make_age_group(series):
    '''
    Function to make the group of ages in interval of 10
    Args:
        series : pandas Series
    Returns:
        a numpy array containing the 
    '''
    
    age_grp = []
    
    for i in series.values :
        age_grp.append(f"{(i//10)*10}-{((10+i)//10)*10-1}")
    
    return np.array(age_grp)



def make_income_group(series):
    '''
    Function to make the group of income in interval of 30000
    Args:
        series : pandas Series
    Returns:
        an array containing the interval range to which the income belongs
    '''
    
    income_grp = []
    
    for i in series.values :
        if not pd.isna(i):
            if 30_000 <= i < 60_000 :
                income_grp.append('Low')
            elif 60_000 <= i < 90_000 :
                income_grp.append('Average')
            elif 90_000 <= i <= 120_000:
                income_grp.append('High')
        else:
            income_grp.append(np.nan) 
    
    return np.array(income_grp)