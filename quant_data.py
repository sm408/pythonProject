import pandas as pd

def read_excel_file(file_name):
    """Reads an Excel file and returns a DataFrame."""
    return pd.read_excel(file_name)

def get_quant_columns(df, year_list):
    """Returns the list of columns to select from the DataFrame."""
    return ['table_id'] + ['metric_name', 'source_metric_name'] + [year for year in year_list if year in df.columns]

def select_data(df, quant_columns):
    """Selects the desired columns from the DataFrame."""
    return df[quant_columns]

def print_data(df):
    """Prints the DataFrame."""
    print("\n Selected Data:")
    print(df)

def main(file_name,year_list):

    df = read_excel_file(file_name)
    quant_columns = get_quant_columns(df, year_list)
    quant_data = select_data(df, quant_columns)
    
    return quant_data

if __name__ == "__main__":
    file_name = 'test_quantitative.xlsx'
    year_list = [2019, 2020, 2021, 2022, 2023]
    quant_data = main(file_name, year_list)
    print_data(quant_data)