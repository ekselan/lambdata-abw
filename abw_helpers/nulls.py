def nulls(x):
    '''Checks a dataframe for null values and returns the 
    total nans for each column.'''
    print('Null Totals:\n')
    print(x.isnull().sum())
    print('\nNulls sorted:\n')
    print(x.isnull().sum().value_counts())