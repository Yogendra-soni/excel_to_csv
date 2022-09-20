# Excel To CSV file Converter

This Excel to CSV function is invoked usig ht Dsisi.

Input: pandas dataframe object of excel file.
Output: Dictonary of sheet_name as key, and data of that sheet as value '

Below is the example to invoke this daisi

import pydaisi as pyd
import pandas as pd
import openpyxl
excel_to_csv = pyd.Daisi("ysoni/excel_to_csv")

df=pd.ExcelFile(r'full_file_name_with_path.xlsx')
output=excel_to_csv.convert(df)
for sheet in output.value:
    output[sheet].to_csv(f"{sheet}.csv",index=False,header = None)
