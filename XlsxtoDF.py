import pandas as pd
import os.path



File_Path = f"D:\\User\\Desktop\\Dynamic_Programming\\DP2.xlsx"

if os.path.isfile(File_Path):
    print("  File Found  " + File_Path)
    df = pd.read_excel(File_Path, sheet_name = "DP").to_dict('list')
    print(df)

else:
    print("404 NOT FOUND")         



{0: {'餐點': '功夫麵,原汁牛肉麵,叻沙牛肉麵', '整體滿意度': 211, '價格': 340}, 
1: {'餐點': '魷魚羹,花生雞腿堡,石鍋拌飯', '整體滿意度': 207, '價格': 339}, 
2: {'餐點': '魷魚羹,石鍋拌飯,花生雞腿堡', '整體滿意度': 207, '價格': 339}, 
3: {'餐點': '功夫麵,叻沙牛肉麵,原汁牛肉麵', '整體滿意度': 211, '價格': 340}, 
4: {'餐點': '功夫麵,叻沙牛肉麵,魷魚羹', '整體滿意度': 201, '價格': 295}, 
5: {'餐點': '原汁牛肉麵,叻沙牛肉麵,功夫麵', '整體 滿意度': 211, '價格': 340}}