import pandas as pd




# 選過不能再選
# 整體滿意度=(-熱量(正規後)*10)+喜愛程度
# '熱量(正規後)': [1.0, 0.8914728682170543, 0.6449612403100775, 0.5844961240310077, 0.4186046511627907, 0.3875968992248062, 0.23255813953488372, 0.21705426356589147, 0.12403100775193798, 0.10852713178294573, 0.0, 0.0]
# 有預算上限(800)
# 有熱量上限(4000)
# 最少必須保留剩下餐點裡，剩餘天數個最低價格餐點的價格總和元
    # ex  
        # 剩餘天數: 2
        # 剩下餐點: ['叻沙牛肉麵', '石鍋拌飯', '花生雞腿堡', '原汁牛肉麵']
        # 剩下餐點價格: [160, 140, 129, 115]
        # 應該剩下: 115+129元
# 最少必須保留剩下餐點裡，剩餘天數個最低熱量餐點的熱量總和卡


# Dish = {'餐點': ['叻沙牛肉麵', '石鍋拌飯', '花生雞腿堡', '原汁牛肉麵', '炸豬排飯', '咖哩飯', '雞胸肉餐', '雙層牛肉吉士堡', '涼麵', '魷魚羹', '功夫麵', '烤雞排'], 
# '熱量': [945, 875, 716, 677, 570, 550, 450, 440, 380, 370, 300, 300],
# '價格': [160, 140, 129, 115, 110, 120, 135, 105, 60, 70, 65, 60], 
# '喜愛程度': [100, 88, 76, 74, 71, 69, 68, 65, 62, 59, 53, 50], 
# '整體滿意度': [90, 79, 70, 68, 67, 65, 66, 63, 61, 58, 53, 50], 
# '熱量(正規後).1': [1.0, 0.8914728682170543, 0.6449612403100775, 0.5844961240310077, 0.4186046511627907, 0.3875968992248062, 0.23255813953488372, 0.21705426356589147, 0.12403100775193798, 0.10852713178294573, 0.0, 0.0]}

# Dish = {'餐點': ['叻沙牛肉麵', '333', '222', '石鍋拌飯', '花生雞腿堡', '原汁牛肉麵', '炸豬排飯', '咖哩飯', '雞胸肉餐', '雙層牛肉吉士堡', '涼麵', '魷魚羹', '功夫麵', '烤雞排'], 
# '熱量': [945, 875, 875, 875, 716, 677, 570, 550, 450, 440, 380, 370, 300, 300],
# '價格': [160, 140, 140, 140, 129, 115, 110, 120, 135, 105, 60, 70, 65, 60], 
# '喜愛程度': [100, 88, 88, 88, 76, 74, 71, 69, 68, 65, 62, 59, 53, 50], 
# '整體滿意度': [90, 79, 79, 79, 70, 68, 67, 65, 66, 63, 61, 58, 53, 50], 
# '熱量(正規後).1': [1.0, 0.8914728682170543, 0.8914728682170543, 0.8914728682170543, 0.6449612403100775, 0.5844961240310077, 0.4186046511627907, 0.3875968992248062, 0.23255813953488372, 0.21705426356589147, 0.12403100775193798, 0.10852713178294573, 0.0, 0.0]}

Dish = {'餐點': ['叻沙牛肉麵', '333', '222', '石鍋拌飯', '花生雞腿堡'], 
'熱量': [945, 875, 875, 875, 716],
'價格': [160, 140, 140, 140, 129], 
'喜愛程度': [100, 88, 88, 88, 76], 
'整體滿意度': [90, 79, 79, 79, 70], 
}






T = 4 # 總期數
Sn = 800 # 總餐費(預算上限)
Sc = 4000 # 總熱量(熱量上限)
S = {} #裝各期各x下的value

Dish = pd.DataFrame(Dish) # 丟進DF方便篩選

for t in range(T, 0, -1): # 建立字典中的字典，每個小字典裝當期值
    S[t] = {}
    for i in range(0 , len(Dish)): 
        S[t][i] = {}
        for I in range(0 , len(Dish)):
            S[t][i][I] = {}

# {3期數: {0上一期: {0這一期: 
for t in range(T, 0, -1):
    if t == T:
        for i in range(0, len(Dish)): 
            S[t][i][0]['餐點'] = Dish['餐點'][i]
            S[t][i][0]['整體滿意度'] = Dish['整體滿意度'][i]
            S[t][i][0]['價格'] = Dish['價格'][i]
            S[t][i][0]['熱量'] = Dish['熱量'][i]
        # print(S)
    else:
        DishList = []
        for I in range(len(S[t + 1])): # 上一期的餐點組合數
            for i in range(len(S[t + 1][I])):  
                # print(S[t+1][I])
                if len(S[t+1][I][0]):
                    if t+1 ==2:
                        print(S[t+1][I])
                    LastDish = sorted(S[t+1][I][0]['餐點'].split(','))
                    Money = int(Dish[(~Dish['價格'].isin(LastDish))].sort_values(by = '價格')[['價格']][:t-1].sum()) # 最低飯錢 
                    Car = int(Dish[(~Dish['熱量'].isin(LastDish))].sort_values(by = '熱量')[['熱量']][:t-1].sum()) # 最低熱量 
                    Dish2 = Dish[(~Dish['餐點'].isin(LastDish)) & 
                        (Dish['價格'] <= Sn - Money - S[t + 1][I][0]['價格']) & 
                        (Dish['熱量'] <= Sc - Car - S[t + 1][I][0]['熱量'])].reset_index()# 濾掉重複、超出預算、超出熱量餐點
                    order = 0
                    for a in range(0, len(Dish2)): # 這一期的餐點組合數
                        ThisDish = sorted((S[t + 1][I][0]['餐點'] + "," + Dish2['餐點'][a]).split(',')) # 過濾重複餐點組合減少運算量
                        if ThisDish not in DishList:
                            S[t][I][order]['餐點'] =  S[t + 1][I][0]['餐點'] + "," + Dish2['餐點'][a]
                            S[t][I][order]['整體滿意度'] = Dish2['整體滿意度'][a] + S[t + 1][I][0]['整體滿意度']
                            S[t][I][order]['價格']  = Dish2['價格'][a] + S[t + 1][I][0]['價格']
                            S[t][I][order]['熱量']  = Dish2['熱量'][a] + S[t + 1][I][0]['熱量']
                            DishList += [sorted(S[t][I][order]['餐點'].split(','))]
                            order += 1
                else:
                    del S[t+1][I]
    order = 0
    for I in range(len(S[t])):
        MaxS = S[t][I][0]
        for i in range(len(S[t][I])): # 找出當下最佳解
            
            if i in S[t][I] :
                if len(S[t][I][i]) and t != T:
            # if len(S[t][I][i]) and t != T:

                    if S[t][I][i]['整體滿意度'] >= MaxS['整體滿意度'] and sorted(S[t][I][i]['餐點'].split(',')) != sorted(MaxS['餐點'].split(',')): # 複數最佳解
                        S[t][I + order] = {0: S[t][I][i]}
                        order += 1
                else:
                    del S[t][I][i] # 清掉多餘dict
        S[t][I][0] = MaxS  # 只留最大值組合


# print(S[2])

Opt = {} 
for t in range(T, 0, -1):
    Opt[t] = {}
    Order = 0
    Max = []
    for i in range(len(S[t])): # 找出該組合最大值
        if '整體滿意度' in S[t][i][0]:
            Max += [S[t][i][0]['整體滿意度']]
    Max = max(Max)
    for i in range(len(S[t])):
        if '整體滿意度' in S[t][i][0]:
            if S[t][i][0]['整體滿意度'] == Max:
                Opt[t][Order] = S[t][i]
                Order += 1

# print(Opt) 

{4: {0: {0: {'餐點': '叻沙牛肉麵', '整體滿意度': 90, '價格': 160, '熱量': 945}}, 
    1: {0: {'餐點': '333', '整體滿意度': 79, '價格': 140, '熱量': 875}}, 
    2: {0: {'餐點': '222', '整體滿意度': 79, '價格': 140, '熱量': 875}}, 
    3: {0: {'餐點': '石鍋拌飯', '整體滿意度': 79, '價格': 140, '熱量': 875}}, 
    4: {0: {'餐點': '花生雞腿堡', '整體滿意度': 70, '價格': 129, '熱量': 716}}}, 
3: {0: {0: {'餐點': '叻沙牛肉麵,333', '整體滿意度': 169, '價格': 300, '熱量': 1820}}, 
    1: {0: {'餐點': '333,222', '整體滿意度': 158, '價格': 280, '熱量': 1750}, 
    1: {'餐點': '333,石鍋拌飯', '整體滿意度': 158, '價格': 280, '熱量': 1750}, 
    2: {'餐點': '333,花生雞腿堡', '整體滿意度': 149, '價格': 269, '熱量': 1591}}, 
    2: {0: {'餐點': '333,石鍋拌飯', '整體滿意度': 158, '價格': 280, '熱量': 1750}}, 
    3: {0: {'餐點': '石鍋拌飯,花生雞腿堡', '整體滿意度': 149, '價格': 269, '熱量': 1591}}}, 
2: {0: {0: {'餐點': '叻沙牛肉麵,333,222', '整體滿意度': 248, '價格': 440, '熱量': 2695}}, 
    1: {0: {'餐點': '333,222,石鍋拌飯', '整體滿意度': 237, '價格': 420, '熱量': 2625}, 
    1: {'餐點': '333,222,花生雞腿堡', '整體滿意度': 228, '價格': 409, '熱量': 2466}}, 
    2: {0: {'餐點': '333,石鍋拌飯,花生雞腿堡', '整體滿意度': 228, '價格': 409, '熱量': 2466}}, 
    3: {0: {'餐點': '石鍋拌飯,花生雞腿堡,叻沙牛肉麵', '整體滿意度': 239, '價格': 429, '熱量': 2536}, 
    1: {'餐點': '石鍋拌飯,花生雞腿堡,222', '整體滿意度': 228, '價格': 409, '熱量': 2466}}}, 
1: {0: {0: {'餐點': '叻沙牛肉麵,333,222,石鍋拌飯', '整體滿意度': 327, '價格': 580, '熱量': 3570}, 
    1: {'餐點': '叻沙牛肉麵,333,222,花生雞腿堡', '整體滿意度': 318, '價格': 569, '熱量': 3411}}, 
    1: {0: {'餐點': '333,222,石鍋拌飯,花生雞腿堡', '整體滿意度': 307, '價格': 549, '熱量': 3341}}, 
    2: {0: {'餐點': '333,石鍋拌飯,花生雞腿堡,叻沙牛肉麵', '整體滿意度': 318, '價格': 569, '熱量': 3411}}, 
    3: {0: {'餐點': '石鍋 拌飯,花生雞腿堡,叻沙牛肉麵,222', '整體滿意度': 318, '價格': 569, '熱量': 3411}}, 
    4: {0: {}}}}