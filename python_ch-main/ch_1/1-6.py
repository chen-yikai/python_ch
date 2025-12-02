import random

rank=[0,0,0] # 平手、贏、輸的次數統計
typeText=["剪刀","石頭","布"]  # 出拳選項
stateText=["平手","你贏了","你輸了"]  # 勝負結果
while True:  # 剪刀石頭布遊戲主迴圈
    print(f"勝負統計:你贏了{rank[1]}次，你輸了{rank[2]}次，平手{rank[0]}次")
    user=int(input("請選擇:(1)剪刀 (2)石頭 (3)布 (4)結束:"))
    npc=random.randint(1,3)  # 電腦隨機出拳
    state=0 # 勝負狀態 0:平手 1:贏 2:輸
    if user==4: break  # 結束遊戲
    if npc==user: state=0  # 平手判斷
    elif user==1:  # 使用者出剪刀
        if npc==3: state=1  # 剪刀贏布
        else: state=2       # 剪刀輸石頭
    elif user==2:  # 使用者出石頭
        if npc==1:state=1   # 石頭贏剪刀
        else: state=2       # 石頭輸布
    elif user==3:  # 使用者出布
        if npc==2: state=1  # 布贏石頭
        else: state=2       # 布輸剪刀
    rank[state]+=1  # 統計更新
    print(f"電腦出了:{typeText[npc-1]}，{stateText[state]}!!\n")