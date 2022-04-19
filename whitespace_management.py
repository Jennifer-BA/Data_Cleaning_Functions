import pandas as pd

def remove_whitespace(df):
    """Returns a dataframe with leading and trailing whitespace removed"""
    
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    
    return df