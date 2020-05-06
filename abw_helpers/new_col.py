def new_col(l, data):
    ''' Single function to take a list, turn it into a series and
    add it to a dataframe as a new column

    Params: 
        l: a list
            example: animals = [lions, tigers, bears]
        data: a pandas.DataFrame

    Returns: a first 5 rows of pandas.DataFrame with l added 
            as a new column named "new_column"
    '''

    import pandas as pd
    # Turn list into series
    l = pd.Series(l)
    # Add as new column to dataframe
    data['new_column'] = l
    return data.head()