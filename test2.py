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

year_list = ['2019','2020','2021', '2022', '2023']

# Set the column names for df2
df2.columns = ['tablename', '2023', '2022']

# Create a new DataFrame with matching indicators
df_result = df1.copy()
df_result['2022_match'] = False
df_result['2023_match'] = False
print(df_result)

# Iterate through each row of df1
for index, row in df1.iterrows():
    tablename = row['tablename']
    
    # Search for the tablename in df2
    df2_match = df2[df2['tablename'] == tablename]
    
    if not df2_match.empty:
        # Match the data for the corresponding year
        if row['2022'] == df2_match['2022'].iloc[0]:
            df_result.at[index, '2022_match'] = True
        if row['2023'] == df2_match['2023'].iloc[0]:
            df_result.at[index, '2023_match'] = True

print(df_result)