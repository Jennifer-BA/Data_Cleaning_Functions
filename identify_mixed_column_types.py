def get_column_data_types(df):  
    """Returns a dictionary of each column listing the data types within the column"""
    
    multiple_types = {}
    
    for col in df.columns:
        types_df = df[col].apply(lambda x:x.__class__).value_counts()
        
        if types_df.shape[0] > 1:
            multiple_types[col] = types_df.index.values.tolist()
            
    return multiple_types


def has_multi_types_within_col(df):  
    """Returns if any column in the df has multiple data types within the column"""
    
    return len(get_column_data_types(df).keys()) > 0