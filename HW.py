import pandas as pd



# 選過不能再選
# 整體滿意度=(-熱量(正規後)*0.1)+喜愛程度
# '熱量(正規後)': [1.0, 0.8914728682170543, 0.6449612403100775, 0.5844961240310077, 0.4186046511627907, 0.3875968992248062, 0.23255813953488372, 0.21705426356589147, 0.12403100775193798, 0.10852713178294573, 0.0, 0.0]
# 預算上限800/7*3 = 342.857
# 不考慮熱量上限
# 最少必須保留60*剩餘天數元
# 60為每日最低飯錢

# Dish = {'餐點': ['叻沙牛肉麵', '石鍋拌飯', '花生雞腿堡', '原汁牛肉麵', '炸豬排飯', '咖哩飯', '雞胸肉餐', '雙層牛肉吉士堡', '涼麵', '魷魚羹', '功夫麵', '烤雞排'], 
# '熱量': [945, 875, 716, 677, 570, 550, 450, 440, 380, 370, 300, 300],
# '價格': [160, 140, 129, 115, 110, 120, 135, 105, 60, 70, 65, 60], 
# '喜愛程度': [100, 88, 76, 74, 71, 69, 68, 65, 62, 59, 53, 50], 
# '整體滿意度': [90, 79, 70, 68, 67, 65, 66, 63, 61, 58, 53, 50], 
# '熱量(正規後).1': [1.0, 0.8914728682170543, 0.6449612403100775, 0.5844961240310077, 0.4186046511627907, 0.3875968992248062, 0.23255813953488372, 0.21705426356589147, 0.12403100775193798, 0.10852713178294573, 0.0, 0.0]}
Dish = {'餐點': ['叻沙牛肉麵', '石鍋拌飯', '花生雞腿堡', '原汁牛肉麵', '魷魚羹', '功夫麵'], 
'熱量': [945, 875, 716, 677, 370, 300], 
'價格': [160, 140, 129, 115, 70, 65], 
'喜愛程度': [100, 88, 76, 74, 59, 53], 
'整體滿意度': [90, 79, 70, 68, 58, 53]}

T = 3 # 總期數
Sn = 342 # 剩下的餐費

S = {} #裝各期各x下的value
V = {}
MinP = min(Dish['價格']) #每日最低預算
Dish = pd.DataFrame(Dish)
# print(Dish)


for t in range(T, 0, -1): # 建立字典中的字典，每個小字典裝當期值
    S[t] = {}
    V[t] = {}
    for i in range(0 , len(Dish)): 
        S[t][i] = {}
        V[t][i] = {}
        for I in range(0 , len(Dish)):
            S[t][i][I] = {}
# {3期數: {0上次選的餐點: {0現在選的餐點: 
for t in range(T, 0, -1):
    if t == T:
        for i in range(0, len(Dish)): 
            S[t][i][0]['餐點'] = Dish['餐點'][i]
            S[t][i][0]['整體滿意度'] = Dish['整體滿意度'][i]
            S[t][i][0]['價格'] = Dish['價格'][i]
    else:
        for I in range(len(S[t + 1])): # 上一期的餐點組合數
            # Dish2 = Dish[(~Dish['餐點'].isin([Dish['餐點'][I]]))].reset_index()# 濾掉重複、超出預算餐點
            # Dish2 = Dish[(~Dish['餐點'].isin([Dish['餐點'][I]])) & (Dish['價格'] <= Sn-((t-1)* MinP)-Dish['價格'][I])].reset_index()# 濾掉重複、超出預算餐點
            # # print(t + 1, S[t + 1])
            for i in range(len(S[t + 1][I])): 
                if len(S[t + 1][I][i]):
                    # print(S[t + 1][I][i])

                    Dish2 = Dish[(~Dish['餐點'].isin(S[t+1][I][i]['餐點'].split(",")))].reset_index()
                    for a in range(0, len(Dish2)):
                        print(S[t][I][a])
                        S[t][I][a]['餐點'] = Dish2['餐點'][a] + "," + S[t + 1][I][i]['餐點']
                        S[t][I][a]['整體滿意度'] = Dish2['整體滿意度'][a] + S[t + 1][I][i]['整體滿意度']
                        S[t][I][a]['價格']  = Dish2['價格'][a] + S[t + 1][I][i]['價格']
                        print(S[t][I][a])

                


    for I in range(len(S[t])):
        MaxS = S[t][I][0]
        for i in range(len(S[t][I])):
            if len(S[t][I][i]):
                if S[t][I][i]['整體滿意度'] > MaxS['整體滿意度']:
                    MaxS = S[t][I][i]
            else:
                del S[t][I][i]
        # print1    (MaxS)
        S[t][I] = MaxS
    # print(S[t])
# print(S[2])            
                
# 
            # if len(S[t][I][i]) > 1 :

            #     print(S[t][I])
    #     print(v)
        # if S[t][v] == minval:
        #     if t not in K:
        #         K[t] = [v[1]]  #第t期的最佳解是X=x
        #     else:
        #         K[t].append(v[1])
                # print(S[t])
                        
            # print(S[3])
    # print(S)       
        #     aa += [Dish2['價格'][i]]
          
        # Xn += [aa]    
        # print(Xn)
            # S[t][t, i] = Dish2['整體滿意度'][i]
# print(S)
# print(Xn)    
# print(D)
        # print(Dish.iloc[i])

        
    # maxval = max(S[t].values()) #找出當期最大值 
    # print(S[t])
    # print(maxval)
    # Index = Dish['整體滿意度'].index(maxval) #找出當期最大值為第幾期
    # print(Index)



# for t in range(T-1, 0, -1):
#     for i in range(0 , len(Dish[(~Dish['餐點'].isin(Xn)) & (Dish['價格'] <= Sn-((t-1)* MinP))])): # 沒有被選過且價格<=預算的餐點
#         S[t][t, i] = Dish['整體滿意度'][i]
        
#         # print(Dish.iloc[i])

        
#     maxval = max(S[t].values()) #找出當期最大值 
#     print(S[t])
#     print(maxval)
#     Index = Dish['整體滿意度'].index(maxval) #找出當期最大值為第幾期
#     print(Index)
#     Xn.append(Dish[Index])
#     R[t] = maxval # 當期最小的cost 
#     # for v in S[t]:
#     #     if S[t][v] == maxval:
#     #         if t not in K:
#     #             K[t] = [v[1]]  #第t期的最佳解是X=x
#     #         else:
#     #             K[t].appenXn(v[1])
# print(S)
# print(Xn)
# print('----'*10)
# print(K)
# print('----'*10)
# print(R)











<<<<<<< HEAD
# cSet = 300 
# cMar = 100
# cPen = 1600
=======
>>>>>>> e09c3f28606fccfbc462dc3b3922f165e24b77f6



# CP = {}
# R = {}  #裝各期的recursive，即該期最佳cost
# S = {} #裝各期各x下的value
# K = {} #裝各期最佳key值
# X = 6 # 商品最大數量
# T = 3 
# for t in range(T, 0, -1): # 建立字典中的字典，每個小字典裝當期值
#     S[t] = {}
# for t in range(T, 0, -1): # 執行backward induction
#     for x in range(0 , X+1): # 所有的生產量都嘗試看看
#         if t == T: # 如果現在是最後一期
#             if x == 0 :
#                 reward = 0
#             else:
#                 reward = cSet + x * cMar
#             value = reward + ((1/2)**x) * 1600
#         else: # 否則
#             if x == 0:
#                 reward = 0
#             else:
#                 reward = cSet + x * cMar
#             value = reward + ((1/2)**x) * R[t+1]
#         S[t][t, x] = value # 紀錄當下cost
        
#     minval = min(S[t].values()) #找出當期最小值 
#     R[t] = minval # 當期最小的cost
    
<<<<<<< HEAD
#     for v in S[t]:
#         if S[t][v] == minval:
#             if t not in K:
#                 K[t] = [v[1]]  #第t期的最佳解是X=x
#             else:
#                 K[t].append(v[1])
=======
    # for v in S[t]:
    #     if S[t][v] == minval:
    #         if t not in K:
    #             K[t] = [v[1]]  #第t期的最佳解是X=x
    #         else:
    #             K[t].append(v[1])
>>>>>>> e09c3f28606fccfbc462dc3b3922f165e24b77f6
# print(K)
# print('----'*10)
# print(R)
# print('----'*10)
# for i in S:
<<<<<<< HEAD
#     print(S[i])
=======
#     print(S[i])
>>>>>>> e09c3f28606fccfbc462dc3b3922f165e24b77f6
