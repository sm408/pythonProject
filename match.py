import pandas as pd
import quant_data
import all_table_data

quant_file_name = 'test_quantitative.xlsx'
all_table_file_name = 'test_all_table.xlsx'
table_name = "balance_sheet"
year_list = [2019, 2020, 2021, 2022, 2023]
quant_data = quant_data.main(quant_file_name, year_list)
all_table_data = all_table_data.main(all_table_file_name, year_list, table_name)

def get_found_years(df, year_list):
    # Get the year columns from df that are also in year_list
    found_years = [col for col in df.columns if col in year_list]
    return found_years

found_years = get_found_years(all_table_data, year_list)
# print("\n Found Years:")
# print(found_years)

# Convert the data types to numeric for the columns in found_years
all_table_data[found_years] = all_table_data[found_years].apply(pd.to_numeric, errors='coerce')
quant_data[found_years] = quant_data[found_years].apply(pd.to_numeric, errors='coerce')

# print("\n Quantitative Data:")
# print(quant_data)

# print("\n All Table Data:")
# print(all_table_data)


# #print headers of all_table_data and quant_data
# print("\n Headers of All Table Data:")
# print(all_table_data.columns)

# print("\n Headers of Quantitative Data:")
# print(quant_data.columns)

# all_table_data might have columns that dont have headings, give them headings as column1, column2, column3, etc if they are blank
all_table_data.columns = [f'column{i}' if col == '' else col for i, col in enumerate(all_table_data.columns, 1)]

# print("\n Headers of All Table Data after renaming:")
# print(all_table_data)

# Create a new DataFrame with matching indicators
matched_result = quant_data.copy()
for year in found_years:
    matched_result[f'{year}_match'] = False
    matched_result[f'{year}_alltable'] = None

# Skip the first row of all_table_data
all_table_data = all_table_data.iloc[1:]

# # Iterate through each row of quant_data
# for index, row in quant_data.iterrows():
#     source_metric_name = row['source_metric_name']

#     # Search for the source_metric_name in all_table_data
#     all_table_data_match = all_table_data[all_table_data['column1'] == source_metric_name]
    
#     if not all_table_data_match.empty:
#         # Match the data for each year present in all_table_data
#         print("\n All Table Data Match:")

#         print(all_table_data_match)

#         for year in found_years:
#             if row[year] == all_table_data_match[year].iloc[0]:
#                 matched_result.at[index, f'{year}_match'] = True
#                 print(f"Matched value from df1 for {year}: {row[year]}")
#             matched_result.at[index, f'{year}_alltable'] = matched_result[year].iloc[0]

# print("\n ")


# Iterate through each row of quant_data
for index, row in quant_data.iterrows():
    source_metric_name = row['source_metric_name']

    # Search for the source_metric_name in all_table_data
    all_table_data_match = all_table_data[all_table_data['column1'] == source_metric_name]
    
    if not all_table_data_match.empty:
        # Match the data for each year present in all_table_data
        print("\n All Table Data Match:")

        print(all_table_data_match)

        for year in found_years:
            if row[year] == all_table_data_match[year].iloc[0]:
                matched_result.at[index, f'{year}_match'] = True
                print(f"Matched value from df1 for {year}: {row[year]}")
            matched_result.at[index, f'{year}_alltable'] = all_table_data_match[year].iloc[0]

print("\n ")

print(matched_result)