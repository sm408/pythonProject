import pandas as pd

# Sample data for df1
data1 = {
    'tablename': ['tableA', 'tableB', 'tableC'],
    'metricname': ['metric1', 'metric2', 'metric3'],
    '2022': [10, 20, 30],
    '2023': [15, 25, 35]
}
df1 = pd.DataFrame(data1)

# Sample data for df2
data2 = {
    0: ['tableA', 'tableB', 'tableC'],
    '2023': [15, 26, 35],
    '2022': [10, 21, 30]
}
df2 = pd.DataFrame(data2)

# Set the column names for df2
df2.columns = ['tablename', '2023', '2022']

# Step 1: Match the data in year columns of both tables
df_merged = df1.merge(df2, on='tablename', how='outer')
print(df_merged)

# Step 2: Search for the metricname from df1 in df2
df_merged['metricname_match'] = df_merged['metricname'].isin(df2['tablename'])

# Step 3: Match the corresponding data for the matched rows
df_merged['2022_match'] = df_merged['2022_x'] == df_merged['2022_y']
df_merged['2023_match'] = df_merged['2023_x'] == df_merged['2023_y']

# Step 4: Create a new DataFrame with matching indicators
df_result = df_merged[['tablename', 'metricname', '2022_x', '2023_x', '2022_match', '2023_match']]
df_result.columns = ['tablename', 'metricname', '2022', '2023', '2022_match', '2023_match']

print(df_result)