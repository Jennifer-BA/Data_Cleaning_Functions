import pandas as pd
import numpy as np

def get_column_data_types(col):
    """Returns the list of data types in a column"""
    
    dt = col.apply(lambda x: x.__class__)
    
    return dt.value_counts().index.tolist()


def identify_outliers(col, verbose=False):
    """Returns a true/false index identifying outliers in a column"""
    
    idx_interquartile = None
    
    if len(get_column_data_types(col)) > 1:
        raise TypeError('ERROR: Multiple data types detected.')

    q1 = np.percentile(col, 25, interpolation='lower')
    q3 = np.percentile(col, 75, interpolation='higher')
    iqr = q3 - q1
    minimum = q1 - 1.5 * iqr
    maximum = q3 + 1.5 * iqr

    idx = ((minimum <= col) & (col <= maximum))
    idx_interquartile = idx
        
    return ~idx_interquartile
    
    
def drop_outliers(df, columns=None, verbose=False):
    """Returns a dataframe with all rows with identified outliers removed"""
    
    # Copy the dataframe to not overwrite the dataframe
    df_copy = df.copy()
    
    idx_interquartile = []
    non_numeric_cols = []

    # Iterating through columns using try and except for distinguishing between numerical and categorical columns
    if columns is None:
        print("No columns specified. Attempting to remove outliers from all columns.")
    for col in columns or df_copy.columns:
            
        try:
            idx_interquartile.append(~identify_outliers(df_copy[col], verbose))

        except TypeError as e:
            non_numeric_cols.append(col)
            continue
    
    df_copy = df_copy.loc[np.all(idx_interquartile, axis=0)] 
    
    # Print original and new dataframe
    if len(non_numeric_cols) > 0:
        print(f'Not processing {len(non_numeric_cols)} non-numeric columns: {non_numeric_cols}.')
    print('Original Dataframe Shape: ', str(df.shape))
    print('New Dataframe Shape: ', str(df_copy.shape))

    return df_copy