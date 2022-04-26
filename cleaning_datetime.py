import pandas as pd


def cols_to_datetime(df, date_time_columns, unix_epoch_columns):
    
    for col in date_time_columns:
        df[col] = pd.to_datetime(df[col])
    
    for col in unix_epoch_columns:
        df[col] = pd.to_datetime((pd.to_datetime(df[col], unit='s')).dt.strftime('%Y-%m-%d %H:%M:%S.%f'))
        
    return df


def datetime_convert_inplace(df):
    """Returns a dataframe with object type columns converted to datetime when all non-nan values parse successfully"""
    
    from pandas.errors import ParserError
    
    for col in df.columns[df.dtypes == 'object']:
        try:
            df[col] = pd.to_datetime(df[col])
        except (ParserError, ValueError):
            pass
        
    return df


def read_csv(*args, **kwargs):
    """Returns a dataframe using the arguments for read_csv with datetime_convert_inplace run"""
    
    return datetime_convert_inplace(pd.read_csv(*args, **kwargs))