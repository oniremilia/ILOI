import pandas as pd
import win32com.client

input_path = input("Enter the input file path: ")
pw = input("Enter the password: ")


xlApp = win32com.client.Dispatch("Excel.Application")
xlwb = xlApp.Workbooks.Open(input_path, Password=pw)
xlws = xlwb.Sheets(1)
content = xlws.Range(xlws.Cells(6, 2), xlws.Cells(66)).Value 
dataframe = pd.DataFrame(list(content))

print(dataframe.head())