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


Dish = {'餐點': ['叻沙牛肉麵', '我是素食', '神奇沙拉', '原汁牛肉麵', '炸豬排飯', '咖哩飯', '雞胸肉餐', '素肉全餐', '涼麵(素)', '魷魚羹', '功夫麵', '烤雞排'], 
'熱量': [945, 875, 716, 677, 570, 550, 450, 440, 380, 370, 300, 300],
'價格': [160, 140, 129, 115, 110, 120, 135, 105, 60, 70, 65, 60], 
'喜愛程度': [100, 88, 76, 74, 71, 69, 68, 65, 62, 59, 53, 50], 
'整體滿意度': [90, 79, 70, 68, 67, 65, 66, 63, 61, 58, 53, 50], 
'葷素': ['葷', '素', '素', '葷', '葷', '葷', '葷', '素', '素', '葷', '葷', '葷']}


T = 7 # 總期數
Sn = 800 # 總餐費(預算上限)
Sc = 4000 # 總熱量(熱量上限)
S = {} #裝各期各x下的value
IsVe = "葷" # 先裝葷食
VeDays = 3 # 吃素天數
Dish = pd.DataFrame(Dish) # 丟進DF方便篩選
Opt = {} 
for t in range(T, 0, -1): # 建立字典中的字典，每個小字典裝當期值
    S[t] = {}
    for i in range(0 , len(Dish)): 
        S[t][i] = {}
        for I in range(0 , len(Dish)):
            S[t][i][I] = {}

# {3期數: {0上一期: {0這一期: 
for t in range(T, 0, -1):
    if t == T:
        Dish2 = Dish[Dish['葷素'] == IsVe].reset_index()
        for i in range(0, len(Dish2)): 
            S[t][i][0]['餐點'] = Dish2['餐點'][i]
            S[t][i][0]['整體滿意度'] = Dish2['整體滿意度'][i]
            S[t][i][0]['價格'] = Dish2['價格'][i]
            S[t][i][0]['熱量'] = Dish2['熱量'][i]
    else:
        DishList = []
        if t <= VeDays: # 是否要開始裝素食
            IsVe = "素" # 後裝素食
        for I in range(len(S[t + 1])): # 上一期的餐點組合數
            for i in range(len(S[t + 1][I])):  
                LastDish = sorted(S[t+1][I]['餐點'].split(','))
                Money = int(Dish[(~Dish['價格'].isin(LastDish))].sort_values(by = '價格')[['價格']][:t-1].sum()) # 最低飯錢 
                Car = int(Dish[(~Dish['熱量'].isin(LastDish))].sort_values(by = '熱量')[['熱量']][:t-1].sum()) # 最低熱量 
                Dish2 = Dish[(~Dish['餐點'].isin(LastDish)) & 
                    (Dish['葷素'] == IsVe) & 
                    (Dish['價格'] <= Sn - Money - S[t + 1][I]['價格']) & 
                    (Dish['熱量'] <= Sc - Car - S[t + 1][I]['熱量'])].reset_index()# 濾掉重複、超出預算、超出熱量餐點、葷或素
                Max = []
                order = 0
                for a in range(0, len(Dish2)): # 這一期的餐點組合數
                    ThisDish = sorted((S[t + 1][I]['餐點'] + "," + Dish2['餐點'][a]).split(',')) # 過濾重複餐點組合減少運算量
                    if ThisDish not in DishList:
                        S[t][I][order]['餐點'] =  S[t + 1][I]['餐點'] + "," + Dish2['餐點'][a]
                        S[t][I][order]['整體滿意度'] = Dish2['整體滿意度'][a] + S[t + 1][I]['整體滿意度']
                        S[t][I][order]['價格']  = Dish2['價格'][a] + S[t + 1][I]['價格']
                        S[t][I][order]['熱量']  = Dish2['熱量'][a] + S[t + 1][I]['熱量']
                        Max += [S[t][I][order]['整體滿意度']]
                        DishList += [sorted(S[t][I][order]['餐點'].split(','))]
                        order += 1

    for I in range(len(S[t])):
        MaxS = S[t][I][0]
        for i in range(len(S[t][I])): # 找出當下最佳解
            if len(S[t][I][i]):
                if S[t][I][i]['整體滿意度'] > MaxS['整體滿意度']:
                    MaxS = S[t][I][i]
            else:
                del S[t][I][i] # 清掉多餘dict
        S[t][I] = MaxS  # 只留最大值組合

    for i in range(len(S[t])):
        if len(S[t][i]):
            MaxS = S[t][i]
            break
    Order = 0
    for i in range(len(S[t])):
        if len(S[t][i]):
            
            if S[t][i]['整體滿意度'] >= MaxS['整體滿意度']:
                MaxS = S[t][i] 
                Opt[t] = {Order: MaxS}
                if S[t][i]['整體滿意度'] == MaxS['整體滿意度']:                  
                    Order += 1
 

print(Opt)            
                
