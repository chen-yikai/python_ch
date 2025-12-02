#%% 基本函式
def avg(x,y):
    return (x+y) /2

a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
print(f"The average of a and b is {avg(a,b)}")
#%% 等差數列練習
import math

def progress(a1,d,n):
    an=a1+(n-1)*d
    sn=(n*(a1+an))/2
    return an,sn
a1=int(input("輸入數列的首項: "))
d=int(input("輸入數列的公差: "))
n=int(input("輸入數列的項數: "))
an,sn=progress(a1,d,n)
print(f"等差數列的末項為  {an}，和為 {sn}")
#%% 無回傳值自訂函式
def printChar(ch,n):
    for i in range(n):
        print(str(ch),end="")
    print()
ch1='A'
n1=12
printChar(ch1,n1)
printChar("$",15)
printChar("B",n1+4)
#%% eval
x='5*2'
print(type(x))
print(x)
e=eval(x)
print(type(e))
print(e)
#%% 遞迴階乘
def d(a):
    if a <= 1:
        return 1
    else:
        return a * d(a-1)
n=int(input("請輸入要計算的階乘數值: "))
fac=d(n)
print(f"{n}! = {fac}")
#%% 費事數列
def fibi(a):
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return fibi(a - 1) + fibi(a - 2)
while True:
    print()
    x=int(input("請問要計算費式數列的第幾項係數為: "))

    print(f"費氏數列第{x}項的係數值為{fibi(x-1)}")
    print()
    opt=input("請問是否再次計算(y/n)? ")
    if opt == "y": continue
    elif opt == "n": break
#%%傳遞串列元素
def Triple(x,y):
    x=x*3
    y=y*3
    print("In function")
    print(f"x={x}\ty={y}")
array=[1,2,3,4,5]
x=10
y=array[3]
print("Before")
print(f"x={x}\ty={y}")
Triple(x,y)
print("After")
print(f"x={x}\ty={y}")
#%% 傳遞串列元素(傳值呼叫)
def Triple(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * 3
    print("In function")
    print(f"串列 arr={arr}")
arr=[2,3,4,5,6]
print("Before")
print(f"串列 arr={arr}")
Triple(arr)
print("After")
print(f"串列 arr={arr}")
#%% 變數覆蓋
def subpro():
    v1=31
    v3=33
    print("全域、區域")
    print(f"v1={v1}\tv3={v3}")
    print()
v1=100
v2=200
print("全域")
print(f"v1={v1}\tv2-{v2}")
print("")
subpro()
print("全域")
print(f"v1={v1}\tv2={v2}")
#%% global宣告變數
def subpro():
    global n
    n=n+10
    m=20
    print("\nsubpro---")
    print(f"n = {n}, m = {m}")

n=100
m=200
print("\nmain---")
print(f"n = {n}, m = {m}")

subpro()

print("\nmain---")
print(f"n = {n}, m = {m}")