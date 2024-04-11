import pandas as pd

# def read_excel_file(file_name):
#     return pd.read_excel(file_name)

def read_excel_file(file_name, table_name):
    with pd.ExcelFile(file_name) as xls:  # Ensure the file is closed after reading
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            if df.isin([table_name]).any().any():
                return df
    return pd.DataFrame()

def get_last_valid_column(df):
    last_valid_column_name = df.iloc[4].last_valid_index()
    return df.columns.get_loc(last_valid_column_name)

# def select_and_clean_data(df, start_col_index, end_col_index):
#     df = df.iloc[4:, start_col_index:end_col_index+1]
#     df = df.fillna('')
#     df.columns = df.iloc[0]
#     df = df[1:].reset_index(drop=True)
#     return df

def select_and_clean_data(df, start_col_index, end_col_index):
    df = df.iloc[4:, start_col_index:end_col_index+1]
    df.fillna('', inplace=True)  # Modify the DataFrame in place
    df.columns = df.iloc[0]
    df = df[1:]
    df.reset_index(drop=True, inplace=True)  # Modify the DataFrame in place
    return df

# def clean_year_columns(df, year_list):
#     for col in year_list:
#         if col in df.columns:
#             df[col] = df[col].astype(str)
#             df[col] = pd.to_numeric(df[col].replace('[^-\\d.]', '', regex=True))
#     return df

def clean_year_columns(df, year_list):
    for col in year_list:
        if col in df.columns:
            df[col] = df[col].astype(str)
            df[col] = pd.to_numeric(df[col].replace('[^-\\d.]', '', regex=True), errors='coerce')
    return df






# def main(file_name, year_list):
#     all_table_data = read_excel_file(file_name)
#     start_col_index = 3
#     end_col_index = get_last_valid_column(all_table_data)
#     all_table_data = select_and_clean_data(all_table_data, start_col_index, end_col_index)
#     all_table_data = clean_year_columns(all_table_data, year_list)
#     return all_table_data

def main(file_name, year_list, table_name):
    all_table_data = read_excel_file(file_name, table_name)
    if all_table_data.empty:
        print(f"No sheet found containing '{table_name}'")
        return all_table_data
    start_col_index = 3
    end_col_index = get_last_valid_column(all_table_data)
    all_table_data = select_and_clean_data(all_table_data, start_col_index, end_col_index)
    all_table_data = clean_year_columns(all_table_data, year_list)
    
    return all_table_data

if __name__ == "__main__":
    year_list = [2019, 2020, 2021, 2022, 2023]
    table_name = "balance_sheet"
    df = main('test_all_table.xlsx', year_list, table_name)
    print("\n Cleaned Data:")
    print(df)
