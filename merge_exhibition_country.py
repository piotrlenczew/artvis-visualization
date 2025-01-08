import pandas as pd

exhibitions = pd.read_csv('exhibitions.csv')
countries = pd.read_csv('country_names.csv')

countries = countries[['id', 'short_name', 'name']]
countries = countries.rename(columns={'id': 'country_id', 'short_name': 'country', 'name': 'country_name'})

exhibitions_with_countries = pd.merge(exhibitions, countries, on='country', how='left')

exhibitions_with_countries.to_csv('exhibitions_with_countries.csv', index=False)
