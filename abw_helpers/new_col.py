import pandas as pd

def new_col(l, data):
    ''' Single function to take a list, turn it into a series and
    add it to a dataframe as a new column

    Params: 
        data: a pandas.DataFrame
            example: df = pd.DataFrame({'a':[1,2,3]})
        l: a python list
            example: animals = ['lions', 'tigers', 'bears']

    Returns: first 5 rows of pandas.DataFrame with l added 
            as a new column named "new_column"
    '''

    # Turn list into series
    l = pd.Series(l)
    # Add as new column to dataframe
    self['new_column'] = l
    return self.head()