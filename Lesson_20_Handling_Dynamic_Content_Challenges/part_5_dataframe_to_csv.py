import pandas as pd

data = [... ]  # Assume this is your fetched JSON data
df = pd.DataFrame(data)
df.to_csv('scraped_data.csv', index=False)
