# lambdata-abw

A python package that facilitates adding columns and getting null values. Includes PlusFrame class
and two methods.

    PlusFrame: A custom pandas.DataFrame

    new_col(): Single function to take a list, turn it into a series and add it to a dataframe as a new column

    nulls(): Checks a dataframe for null values and returns the total nans for each column.

## Installation

Shell:
```
pip install -i https://test.pypi.org/simple/ lambdata-abw==3.2
```


Python notebook:
```
!pip install -i https://test.pypi.org/simple/ lambdata-abw==3.2
```

## Usage

Python:

    PlusFrame: ```from abw_helpers.plusframe import PlusFrame```
        
        Example: 
            pf = PlusFrame({'heroes': ['dr strange', 'spider man', 'silver surfer', 'thor']})

    new_col(): ```pf.new_col(list)```

        Params: l: a python list

            Example: animals = ['lions', 'tigers', 'bears']
        
        Returns: first 5 rows of PlusFrame with l added as a new column named "new_column"

    nulls(): ```pf.nulls()```

        Returns: Sum of nulls in dataframe by column
