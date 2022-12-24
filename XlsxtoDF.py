import pandas as pd
import os.path



File_Path = f"D:\\User\\Desktop\\Dynamic_Programming\\DP2.xlsx"

if os.path.isfile(File_Path):
    print("  File Found  " + File_Path)
    df = pd.read_excel(File_Path, sheet_name = "DP").to_dict('list')
    print(df)

else:
    print("404 NOT FOUND")         



{0: {0: {'餐點': '石鍋拌飯,叻沙牛肉麵', '整體滿意度': 169, '價格': 300}, 1: {'餐點': '花生雞腿堡,叻沙牛肉麵', '整體滿意度': 160, '價格': 289}, 2: {'餐點': '原汁牛肉麵,叻沙牛肉麵', '整體滿意度': 158, '價格': 275}, 3: {'餐點': '魷魚羹,叻沙牛肉麵', '整體滿意度': 148, '價格': 230}, 4: {'餐點': '功夫麵,叻沙牛肉麵', '整體滿意度': 143, '價格': 225}}, 
1: {0: {'餐點': '叻沙牛肉麵,石鍋拌飯', '整體滿意度': 169, '價格': 300}, 1: {'餐點': '花生雞腿堡,石鍋拌飯', '整體滿意度': 149, '價格': 269}, 2: {'餐點': '原汁牛肉麵,石鍋拌飯', '整體滿意度': 147, '價格': 255}, 3: {'餐點': '魷魚羹,石鍋拌飯', '整體滿意度': 137, '價格': 210}, 4: {'餐點': '功夫麵,石鍋拌飯', '整體滿意度': 132, '價格': 205}}, 
2: {0: {'餐點': '叻沙牛肉麵,花生雞腿堡', '整體滿意度': 160, '價格': 289}, 1: {'餐點': '石鍋拌飯,花生雞腿堡', '整體滿意度': 149, '價格': 269}, 2: {' 餐點': '原汁牛肉麵,花生雞腿堡', '整體滿意度': 138, '價格': 244}, 3: {'餐點': '魷魚羹,花生雞腿堡', '整體滿意度': 128, '價格': 199}, 4: {'餐點': '功夫麵,花生雞腿堡', '整體滿意度': 123, '價格': 194}}, 
3: {0: {'餐點': '叻沙牛肉麵,原汁牛肉麵', '整體滿意度': 158, '價格': 275}, 1: {'餐點': '石鍋拌飯,原汁牛肉麵', '整體滿意度': 147, '價格': 255}, 2: {'餐點': '花生雞腿堡,原汁牛肉麵', '整體滿意度': 138, '價格': 244}, 3: {'餐點': '魷魚羹,原汁牛肉麵', '整體滿意度': 126, '價格': 185}, 4: {'餐點': '功夫麵,原汁牛肉麵', '整體滿意度': 121, '價格': 180}}, 
4: {0: {'餐點': '叻沙牛肉麵,魷魚羹', '整體滿意度': 148, '價格': 230}, 1: {'餐點': '石鍋拌飯,魷魚羹', '整體滿意度': 137, '價格': 210}, 2: {'餐點': '花生雞腿堡,魷魚羹', '整體滿意度': 128, '價格': 199}, 3: {'餐點': '原汁牛肉麵,魷魚羹', '整體滿意度': 126, '價格': 185}, 4: {'餐點': '功夫麵,魷魚羹', '整體滿意度': 111, '價格': 135}}, 
5: {0: {'餐點': '叻沙牛肉麵,功夫麵', '整體滿意度': 143, '價格': 225}, 1: {'餐點': '石鍋拌飯,功夫麵', '整體滿意度': 132, '價格': 205}, 2: {'餐點': '花生雞腿堡,功夫麵', '整體滿意度': 123, '價格': 194}, 3: {'餐點': '原汁牛肉麵,功夫麵', '整體滿意度': 121, '價格': 180}, 4: {'餐點': '魷魚羹,功夫麵', '整體滿意度': 111, '價格': 135}}}


# {0: {0: {'餐點': '石鍋拌飯,功夫麵,叻沙牛肉麵', '整體滿意度': 222, '價格': 365}, 1: {'餐點': '花生雞腿堡,功夫麵,叻沙牛肉麵', '整體滿意度': 213, '價格': 354}, 2: {'餐點': '原汁牛肉麵,功夫麵,叻沙牛肉麵', '整體滿意度': 211, '價格': 340}, 3: {'餐點': '魷魚羹,功夫麵,叻沙牛肉麵', '整體滿意度': 201, '價格': 295}}, 
# 1: {0: {'餐點': '叻沙牛肉麵,功夫麵,石鍋拌飯', '整體滿意度': 222, '價格': 365}, 1: {'餐點': '花生雞腿堡,功夫麵,石鍋拌飯', '整體滿意度': 202, '價格': 334}, 2: {'餐點': '原汁牛肉麵,功夫麵,石鍋拌飯', '整體滿意度': 200, '價格': 320}, 3: {'餐點': '魷魚羹,功夫麵,石鍋拌飯', '整體滿意度': 190, '價格': 275}}, 
# 2: {0: {'餐點': '叻沙牛肉麵,功夫麵,花生雞腿堡', '整體滿意度': 213, '價格': 354}, 1: {'餐點': '石鍋拌飯,功夫麵,花生雞腿堡', '整體滿意度': 202, '價格': 334}, 2: {'餐點': '原汁牛肉麵,功夫麵,花生雞腿堡', '整體滿意度': 191, '價格': 309}, 3: {'餐點': '魷魚羹,功夫麵,花生雞腿堡', '整體滿意度': 181, '價格': 264}}, 
# 3: {0: {'餐點': '叻沙牛肉麵,功夫麵,原汁牛肉麵', '整體滿意度': 211, '價格': 340}, 1: {'餐點': '石鍋拌飯,功夫麵,原汁牛肉麵', '整體滿意度': 200, '價格': 320}, 2: {'餐點': '花生雞腿堡,功夫麵,原汁牛肉麵', '整體滿意度': 191, '價格': 309}, 3: {'餐點': '魷魚羹,功夫麵,原汁牛肉麵', '整體滿意度': 179, '價格': 250}}, 
# 4: {0: {'餐點': '叻沙牛肉麵,功夫麵,魷魚羹', '整體滿意度': 201, '價格': 295}, 1: {'餐點': '石鍋拌飯,功夫麵,魷魚羹', '整體滿意度': 190, '價格': 275}, 2: {'餐點': '花生雞腿堡,功夫麵,魷魚羹', '整體滿意度': 181, '價格': 264}, 3: {'餐點': '原汁牛肉麵,功夫麵,魷魚羹', '整體滿意度': 179, '價格': 250}}, 
# 5: {0: {'餐點': '叻沙牛肉麵,魷魚羹,功夫麵', '整體滿意度': 201, '價格': 295}, 1: {'餐點': '石鍋拌飯,魷魚羹,功夫麵', '整體滿意度': 190, '價格': 275}, 2: {'餐點': '花生雞腿堡,魷魚羹,功夫麵', '整體滿意度': 181, '價格': 264}, 3: {'餐點': '原汁牛肉麵,魷魚羹,功夫麵', '整體滿意度': 179, '價格': 250}}}