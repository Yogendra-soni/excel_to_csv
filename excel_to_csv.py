import xlrd
import csv
import pandas as pd

def convert(df):
    list_of_sheets = df.sheet_names
    output = {}
    print(list_of_sheets)
    for sheet in list_of_sheets:
        data=pd.read_excel(df,sheet_name = sheet,header = None)
        output[sheet] = data
    return output
