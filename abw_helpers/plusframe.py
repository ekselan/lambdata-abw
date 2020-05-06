import pandas as pd
from pandas import DataFrame


class PlusFrame(DataFrame):
    """
    A custom pandas.DataFrame for adding columns and getting null values
    """

    def new_col(self, l):
        ''' Single function to take a list, turn it into a series and
        add it to a dataframe as a new column

        Params: 
            l: a list
                example: animals = ['lions', 'tigers', 'bears']

        Returns: first 5 rows of pandas.DataFrame with l added 
                as a new column named "new_column"
        '''

        # Turn list into series
        l = pd.Series(l)
        # Add as new column to dataframe
        self['new_column'] = l
        return self.head()

    def nulls(self):
        '''Checks a dataframe for null values and returns the
        total nans for each column.

        Returns: Print out of nulls in dataframe by column
        '''
        
        print('\nNull Totals:\n')
        print(self.isnull().sum().value_counts())


if __name__ == "__main__":
    
    animals = ['a','b','c','d','e','f']
    pf = PlusFrame({
        'heroes':['dr strange','spider man','silver surfer','thor','blade','hulk'],
        'villains':['dormamu','mysterio','galactus','ultron','dracula','red hulk']
    })
    print(pf.head())

    print('\n',pf.new_col(animals))

    # print('\n',pf.)

    