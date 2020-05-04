def new_col(l,data):
    ''' Single function to take a list, turn it into a series and 
    add it to a dataframe as a new column'''
    import pandas as pd
    # Turn list into series
    l = pd.Series(l)
    # Add as new column to dataframe
    data['new_column'] = l
    return data.head()