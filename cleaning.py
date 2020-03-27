

## TODO: Functions for cleaning headers, creating new time variables, show variables with missing values, 


def cleanHeaders(df, remove_whitespace=True, replace_dash=False, lowercase=False, uppercase=False):
    '''Function that formats the column headers of a dataframe.
    Arguments:
        df : Pandas DataFrame
            Dataframe to be formatted. 
        remove_whitespace : bool
            Removes whitespaces from column headers.
        replash_dash : bool
            Replaces dashes in column headers with underscores.
        lowercase : bool
            Changes column headers to lowercase.
        uppercase : bool
            Changes column heaedrs to uppercase.
        
    Returns:
        df : Pandas DataFrame
            Formatted dataframe.
    
    '''
    if remove_whitespace:
        df.columns = df.columns.str.strip()
        print('Removing whitespaces ...')
    
    if replace_dash:
        df.columns = df.columns.str.replace('-', '_')
        print('Replacing dashes with underscores ...')

    if lowercase:
        df.columns = df.columns.str.lower()
        print('Changing to lower case ...')
    
    if uppercase:
        df.columns = df.columns.str.upper()
        print('Changing to upper case ...')
    
    print('Dataframe column headers have been formatted.')
    
    return df
    
