from pandas import DataFrame


def add_state_names(my_df):
    # State abbreviation -> Full Name and vice versa
    # FL -> Florida, etc

    new_frame = my_df.copy()
    
    # list or dict with abbrev/name mappings
    names_map = {'CA':'Cali', 'CO':'Colo', 
                'CT':'Conn', 
                'DC':'District of Columbia'}

    # Create a new column which maps the existing column
    # using our names map
    # breakpoint()

    new_frame['name'] = new_frame['abbrev'].map(names_map)
    return new_frame

if __name__ == "__main__":
    
    df = DataFrame({'abbrev':['CA','CO','CT','DC','TX']})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
