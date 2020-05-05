import pandas as pd
from pandas import DataFrame


def add_state_names(my_df):
    """
    Converts a dataframe with a column of state abbreviations,
    adding a corresponding column of state names

    Params: my_df a pandas.DataFrame with a column
    called 'abbrev'.
        Example: DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    
    Returns: a pandas.DataFrame with the original col
    as well as a 'name' column
    """
    
    new_frame = my_df.copy()   
    # list or dict with abbrev/name mappings
    names_map = {'CA': 'Cali', 'CO':'Colo', 
                'CT': 'Conn', 
                'DC': 'District of Columbia'}

    # Create a new column which maps the existing column
    # using our names map
    # breakpoint()

    new_frame['name'] = new_frame['abbrev'].map(names_map)
    return new_frame

if __name__ == "__main__":
    
    df = DataFrame({'abbrev': ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())

    df3 = DataFrame({'a': [1,2,3]})
    breakpoint()

