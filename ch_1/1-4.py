import random
import os

low=int(input("請輸入亂數範圍的下限: "))  # 亂數下限
high=int(input("請輸入亂數範圍的上限: ")) # 亂數上限

while True:  # 無窮迴圈
    ran=random.randint(low, high)  # 產生亂數
    print(f"產生的亂數為 {ran}")
    q=input("請位是否再次產生亂數?(y/n) ")  # 詢問是否繼續
    if q == "n": break  # 跳出迴圈
    
os.system('cls')  # 清除螢幕