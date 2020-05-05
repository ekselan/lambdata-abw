def nulls(x):
    '''Checks a dataframe for null values and returns the
    total nans for each column.

    Params: x: pandas.DataFrame

    Returns: Print out of nulls in dataframe by column
    '''
    print('Null Totals:\n')
    print(x.isnull().sum())
    print('\nNulls Totals:\n')
    print(x.isnull().sum().value_counts())
