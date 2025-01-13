import pandas as pd

# Load CSV
df = pd.read_csv('country_names.csv')

# Convert columns to numbers (you can specify columns that should be numeric)
df['id'] = pd.to_numeric(df['id'], errors='coerce')  # This will convert strings to numbers and replace invalid values with NaN

# Save the modified CSV
df.to_csv('country_names.csv', index=False)
