import pandas as pd

# Sample data for df1
data1 = {
    'tablename': ['tableA', 'tableB', 'tableC'],
    'metricname': ['metric1', 'metric2', 'metric3'],
    '2021': [5, 15, 25],
    '2022': [10, 20, 30],
    '2023': [15, 25, 35]
}
df1 = pd.DataFrame(data1)

# Sample data for df2
data2 = {
    0: ['tableA', 'tableB', 'tableC'],
    '2023': [15, 26, 35],
    '2022': [10, 20, 31]
}
df2 = pd.DataFrame(data2)

year_list = ['2019', '2020', '2021', '2022', '2023']

# Set the column names for df2
df2.columns = ['tablename', '2023', '2022']

# Remove unnecessary years from year_list based on df2 columns
years_in_df2 = list(df2.columns[1:])
year_list = [year for year in year_list if year in years_in_df2]

# Create a new DataFrame with matching indicators
df_result = df1.copy()
for year in year_list:
    df_result[f'{year}_match'] = False


# Iterate through each row of df1
for index, row in df1.iterrows():
    tablename = row['tablename']
    
    # Search for the tablename in df2
    df2_match = df2[df2['tablename'] == tablename]
    print(df2_match)
    
    if not df2_match.empty:
        # Match the data for each year present in df2
        for year in year_list:
            if row[year] == df2_match[year].iloc[0]:
                df_result.at[index, f'{year}_match'] = True
                print(f"Matched value from df1 for {year}: {row[year]}")

print(df_result)