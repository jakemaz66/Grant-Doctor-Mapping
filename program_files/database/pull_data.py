import sqlite3
import pandas as pd


def extract_data(database):

    #Defining my Queries
    query = '''
    SELECT * FROM npi
    '''

    query2 = '''
    SELECT * FROM grants
    '''

    #Connecting to my database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    #Executing my queries
    cursor.execute(query)
    results_npi = cursor.fetchall()  

    cursor.execute(query2)
    results_grants = cursor.fetchall()  

    df_npi = pd.DataFrame(results_npi, columns=['id', 'last_name', 'forename', 'city', 'state', 'country', 'created_at'])
    df_grants = pd.DataFrame(results_grants, columns=['id', 'last_name', 'forename', 'city', 'state', 'country', 'created_at'])

    #Selecting the matching columns
    df = df_npi[['forename', 'last_name', 'city', 'state', 'country']]
    df2 = df_grants[['forename', 'last_name', 'city', 'state', 'country']]

    #Adding prefixes onto the column names
    mapper = {
            'forename': 'grant_forename',
            'last_name': 'grant_last_name',
            'city': 'grant_city',
            'state': 'grant_state',
            'country': 'grant_country',
        }

    mapper2 = {
            'forename': 'npi_forename',
            'last_name': 'npi_last_name',
            'city': 'npi_city',
            'state': 'npi_state',
            'country': 'npi_country',
        }


    df = df.rename(columns=mapper)[mapper.values()]
    df2 = df2.rename(columns=mapper2)[mapper2.values()]

    #Combining the columns
    df_final = pd.concat([df, df2], axis=1)
    return df_final

    cursor.close()
    conn.close()

if __name__ == '__main__':
    df = extract_data(r'C:\Users\jakem\Grant-Doctor-Mapping-1\program_files\data\grant_npi.db')
