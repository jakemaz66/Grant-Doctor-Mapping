import pandas as pd

#Creating simulated dataframe
df = pd.DataFrame(columns=['grant_forename',
                           'grant_last_name',
                            'grant_city',
                            'grant_state',
                            'grant_country',
                            'npi_forename',
                            'npi_last_name',
                            'npi_city',
                            'npi_state',
                            'npi_country',
                            'label'])
#Coming up with lists of data
last_names = ['Smith', 'Johnson', 'Jesse', 'Brown', 'Miller', 'Davis', 'Garcia', 'Chan', 'Li', 'Jackson']
first_names = ['John', 'Mary', 'Robert', 'Patricia', 'Michael', 'Jennifer', 'William', 'Linda', 'David', 'Elizabeth']
first_names_2 = ['Richard', 'Barbara', 'Joseph', 'Susan', 'Thomas', 'Jessica', 'Charles', 'Sarah', 'Christopher', 'Karen']
cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Cincinatti', 'Columbus', 'Pittsburgh', 'Jacksonville', 'Boston']
states = ['NY', 'CA', 'IL', 'TX', 'FL', 'OH', 'OH', 'PA', 'FL', 'MA']

#Adding data for non-matches
for i in range(0, len(first_names)):
    df.loc[len(df)] = {
        'grant_forename': first_names[i],
        'grant_last_name': last_names[i],
        'grant_city': cities[i],
        'grant_state': states[i],
        'grant_country': 'USA',
        'npi_forename': first_names_2[i],
        'npi_last_name': last_names[-i],
        'npi_city': cities[-i],
        'npi_state': states[-i],
        'npi_country': 'USA',
        'label': 0
    }

#Adding data for matches
for i in range(0, len(first_names)):
    df.loc[len(df)] = {
        'grant_forename': first_names[i],
        'grant_last_name': last_names[i],
        'grant_city': cities[i],
        'grant_state': states[i],
        'grant_country': 'USA',
        'npi_forename': first_names[i],
        'npi_last_name': last_names[i],
        'npi_city': cities[i],
        'npi_state': states[i],
        'npi_country': 'USA',
        'label': 1
    }
