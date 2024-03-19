import sqlalchemy
from grants_processing import read_grants_data
from npi_processing import npi_reader


def db():
    """
    This function creates a sqlalchemy engine connection to the database
    """
    engine = sqlalchemy.create_engine(
        'sqlite:///data/grant_npi.db'
    )

    conn = engine.connect()

    return conn

def npi_csv_to_db(csv_path: str):
    """
    This function creates a relational database out of the npi csv dataset
    """

    #Make npi data, have to rename columns, match data types, define bridge table, download beekeeper studio
    df = npi_reader.read(csv_path)

    #Subsetting to desired columns
    df = df[['last_name', 'forename', 'city', 'state', 'country']]

    #Renaming columns to specified names in database table
    mapper = {
        'last_name': 'lastname',
        'forename': 'forename',
        'city': 'city', 
        'state': 'state', 
        'country': 'country'
    }
    df = df.rename(columns=mapper)[mapper.values()]

    #Dropping NaNs to enforce NOT NULL parameter
    df.dropna(inplace=True)

    #Translating pandas dataframe to database
    df.to_sql('npi',
              db(),
              if_exists='append',
              index=False
              #Big Data
              #method = 'multi'
              #chunksize=1000
              )
    
def grants_csv_to_db(year: int):
    """
    This function creates a relational database out of the grants csv dataset
    """

    #Reading in data
    df = read_grants_data.read_grants_year(year)

    #Subsetting to desired columns
    df = df[['last_name', 'forename', 'city', 'state', 'country']]

    #Renaming columns to specified names in database table
    mapper = {
        'last_name': 'lastname',
        'forename': 'forename',
        'city': 'city', 
        'state': 'state', 
        'country': 'country'
    }
    df = df.rename(columns=mapper)[mapper.values()]

    #Dropping NaNs to enforce NOT NULL parameter
    df.dropna(inplace=True)

    #Translating pandas dataframe to database
    df.to_sql('grants',
              db(),
              if_exists='append',
              index=False
              )
    

if __name__ == '__main__':
    
    npi_csv_to_db(r"data\npidata_pfile_20240205-20240211.csv")
    grants_csv_to_db(2022)