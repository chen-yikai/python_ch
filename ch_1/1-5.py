import random;

bottom=1  # 猜數範圍下限
top=100   # 猜數範圍上限
ans=random.randint(bottom, top)  # 產生答案
user=0
count=1  # 猜測次數

print(ans)  # 顯示答案

while True:  # 猜數遊戲主迴圈
    user=int(input(f"猜猜{bottom}~{top}的數字: "))
    if user < bottom or user > top:  # 輸入範圍檢查
        print("賣鬧阿~ 請輸入符和範圍的整數!")
        continue
    elif user > ans:  # 猜太大
        print(f"再小一點，你總共猜了{count}次")
        top=user-1  # 縮小上限範圍
    elif user < ans:  # 猜太小
        print(f"再大一點，你總共猜了{count}次")
        bottom=user+1  # 縮小下限範圍
    elif user == ans:  # 猜對了
        print(f"恭喜猜對~ 答案是{ans} 讚!!")
        print(f"你總共猜了{count}次")
        break
    count+=1  # 次數累加