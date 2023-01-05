import pandas as pd
import os.path


File_Path = "D:\\ALL\\參考\\Dynamic Programming\\DP2.xlsx"

if os.path.isfile(File_Path):
    print("  File Found  " + File_Path)
    df = pd.read_excel(File_Path, sheet_name = "DP").to_dict('list')
    print(df)

else:
    print("404 NOT FOUND")         
