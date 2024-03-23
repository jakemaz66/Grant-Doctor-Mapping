import sqlite3
import pandas as pd


def extract_data(database):
    '''
    This function creates training data for the distance_classifier by pulling data from the grant_npi database,
    using the npi and grants table
    '''

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

    #Creating separate dataframes
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


def extract_data_from_bridge(database):

    '''
    This function creates training data for the distance_classifier by pulling data from the grant_npi database,
    using the npi_grants_bridge bridge table as a way to increase likelihood of matches
    '''

    #Defining my Queries
    query = '''
    SELECT 
        npi.forename AS npi_forename, npi.lastname AS npi_lastname, npi.city AS npi_city, npi.state AS npi_state, npi.country AS npi_country,
        grants.forename AS grants_forename, grants.lastname AS grants_lastname, grants.city AS grants_city, grants.state AS grants_state, grants.country AS grants_country
    FROM npi
    INNER JOIN npi_grants_bridge ON npi.id = npi_grants_bridge.npi_id
    INNER JOIN grants ON npi_grants_bridge.grants_id = grants.id

    '''

    #Connecting to my database
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    #Executing my queries
    cursor.execute(query)
    results_combine = cursor.fetchall()  
 
    #Creating a large dataframe of npi and grants data
    df_both = pd.DataFrame(results_combine, columns=['forename_npi', 'last_name_npi', 'city_npi', 'state_npi', 'country_npi', 
                                                    'forename_grants', 'last_name_grants', 'city_grants', 
                                                    'state_grants', 'country_grants'])

    #Selecting the matching columns and splitting data
    df = df_both[['forename_npi', 'last_name_npi', 'city_npi', 'state_npi', 'country_npi']]
    df2 = df_both[['forename_grants', 'last_name_grants', 'city_grants', 'state_grants', 'country_grants']]

    #Adding prefixes onto the column names
    mapper = {
            'forename_npi': 'grant_forename',
            'last_name_npi': 'grant_last_name',
            'city_npi': 'grant_city',
            'state_npi': 'grant_state',
            'country_npi': 'grant_country',
        }

    mapper2 = {
            'forename_grants': 'npi_forename',
            'last_name_grants': 'npi_last_name',
            'city_grants': 'npi_city',
            'state_grants': 'npi_state',
            'country_grants': 'npi_country',
        }


    df = df.rename(columns=mapper)[mapper.values()]
    df2 = df2.rename(columns=mapper2)[mapper2.values()]

    #Combining the columns
    df_final = pd.concat([df, df2], axis=1)
    return df_final


if __name__ == '__main__':
    df = extract_data(r'C:\Users\jakem\Grant-Doctor-Mapping-1\program_files\data\grant_npi.db')

    df_combine = extract_data_from_bridge(r'C:\Users\jakem\Grant-Doctor-Mapping-1\program_files\data\grant_npi.db')


