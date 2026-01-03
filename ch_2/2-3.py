#%% 基本函式
def avg(x,y):  # 定義計算平均值的函式
    return (x+y) /2  # 回傳平均值

a=int(input("Enter first num: "))  # 輸入第一個數字
b=int(input("Enter second num: "))  # 輸入第二個數字
print(f"The average of a and b is {avg(a,b)}")  # 顯示平均值
#%% 等差數列練習
import math  # 匯入數學模組

def progress(a1,d,n):  # 定義等差數列計算函式
    an=a1+(n-1)*d  # 計算末項
    sn=(n*(a1+an))/2  # 計算等差數列和
    return an,sn

a1=int(input("輸入數列的首項: "))  # 輸入首項
d=int(input("輸入數列的公差: "))  # 輸入公差
n=int(input("輸入數列的項數: "))  # 輸入項數
an,sn=progress(a1,d,n)  # 呼叫函式計算
print(f"等差數列的末項為  {an}，和為 {sn}")  # 顯示結果
#%% 無回傳值自訂函式
def printChar(ch,n):  # 定義列印指定字元指定次數的函式
    for i in range(n):  # 迴圈指定次數
        print(str(ch),end="")  # 連續列印字元（不換行）
    print()  # 換行

ch1='A'  # 指定字元
n1=12  # 指定次數
printChar(ch1,n1)  # 呼叫函式列印12個A
printChar("$",15)  # 顯示15個$
printChar("B",n1+4)  #顯示16個B
#%% eval
x='5*2'  # 定義數學運算字串
print(type(x))  # 顯示類型（字串）
print(x)  # 顯示字串內容
e=eval(x)  # 使用eval計算字串中的運算式
print(type(e))  # 顯示e變數類型
print(e)  # 顯示計算結果
#%% 遞迴階乘
def d(a):  # 定義遞迴階乘函式
    if a <= 1:  # 基底條件
        return 1
    else:
        return a * d(a-1)  # 遞迴呼叫

n=int(input("請輸入要計算的階乘數值: "))  # 輸入要計算的數值
fac=d(n)  # 呼叫函式計算階乘
print(f"{n}! = {fac}")  # 顯示結果
#%% 費氏數列
def fibi(a):  # 取得第i個費氏數列數字
    if a == 0:
        return 1
    elif a == 1:
        return 1
    else:
        return fibi(a - 1) + fibi(a - 2)  # 遞迴計算前兩項之和

while True:  # 無限迴圈
    print()
    x=int(input("請問要計算費氏數列的第幾項係數為: "))  # 輸入項數

    print(f"費氏數列第{x}項的係數值為{fibi(x-1)}")  # 顯示結果
    print()
    opt=input("請問是否再次計算(y/n)? ")  # 詢問是否繼續
    if opt == "y": continue  # 繼續迴圈
    elif opt == "n": break  # 離開迴圈
#%%傳遞串列元素
def Triple(x,y):  # 定義將值乘以3的函式
    x=x*3
    y=y*3
    print("In function")
    print(f"x={x}\ty={y}")

array=[1,2,3,4,5]  # 定義陣列
x=10
y=array[3]  # 取得陣列第3個元素
print("Before")
print(f"x={x}\ty={y}")
Triple(x,y)  # 呼叫函式（原値不會改變）
print("After")
print(f"x={x}\ty={y}")
#%% 傳遞串列元素(傳值呼叫)
def Triple(arr):  # 定義修改陣列的函式
    for i in range(len(arr)):  # 遍歷陣列
        arr[i] = arr[i] * 3  # 將陣列元素乘以3（參考呼叫）
    print("In function")
    print(f"串列 arr={arr}")

arr=[2,3,4,5,6]  # 定義陣列
print("Before")
print(f"串列 arr={arr}")
Triple(arr)  # 呼叫函式（會修改原陣列）
print("After")
print(f"串列 arr={arr}")
#%% 變數覆蓋
def subpro():
    v1=31  # 區域變數（覆蓋全域變數）
    v3=33  # 只在此函式內存在
    print("全域、區域")
    print(f"v1={v1}\tv3={v3}")  # 顯示區域變數
    print()
# 全域變數
v1=100
v2=200
print("全域")
print(f"v1={v1}\tv2-{v2}")  # 顯示全域變數
print("")
subpro()  # 呼叫子程式
print("全域")
print(f"v1={v1}\tv2={v2}")  # 顯示全域變數