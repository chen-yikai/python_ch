#%% 1
print("\n1-1. 輸入並顯示班級座號姓名\n")
className=input("請輸入班級：")
number=input("請輸入座號：")
name=input("請輸入姓名：")
print(f"\n班級:{className}\t\t\t座號:{number}號\t\t\t姓名:{name}\n")
#%% 2
import math

print("\n1-2. 計算直角三角形 面積及斜邊長")
short=int(input("請輸入直角三角形短的邊長："))
long=int(input("請輸入直角三角形長的邊長："))
print(f"\n此直角三角形的面積為{(short*long)/2:.2f}")
print(f"此直角三角形的斜邊長為{math.sqrt(short**2 +long**2):.2f}\n")
#%% 3
print("\n1-3.  6~198範圍內可被8整除的數字有：",end="")
start=6
end=198
for i in range(start,end+1):
    if i % 8 == 0:
        print(i,end=" ")
print()
#%% 4
print("\n1-4. 巢狀迴圈遞增顯示數字1～10\n")
for i in range(1,11):
    for j in range(1,i+1):
        print(j,end="")
    print()
#%% 5
print("\n1-5. 巢狀迴圈遞減顯示7~1個*號\n")
for i in range(1,8):
    for j in range(1,9-i):
        print("*",end="")
    print()