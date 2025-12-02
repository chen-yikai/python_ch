import random

print("\n猜數字")
ans=random.randint(1, 100)
print(f"\n謎底：{ans}")
top=100
bottom=1
count=0
while True:
    guess=int(input(f"\n請猜{bottom} ~ {top}的數字："))
    if guess not in range(bottom,top+1):
        print("賣鬧啊~ 請輸入符合範圍的整數！")
        continue
    else:
        count+=1
    if guess == ans:
        print(f"恭喜猜對了~ 答案是{ans}  讚！！")
        print(f"你總共猜了{count}次")
        break
    if guess < ans:
        bottom=guess
        print(f"再大一點，你總共猜了{count}次")
    if guess > ans: 
        top=guess
        print(f"再小一點，你總共猜了{count}次")