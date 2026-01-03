#%% 元組
tuple1=("kitty",15,"cute")  # 建立元組
print(tuple1)
a,b,c=tuple1  # 將元組元素分別指派給變數
print(a)  # 印出第一個變數
tuple1+=("meow",)  # 新增元組元素
print(tuple1)
print(len(tuple1))  # 印出元組長度
# del(tuple1) # 刪除元組
# print(tuple1) # Error
#%% 數值交換
i=10
b=20
c=5
print(f"交換前 a={a} b={b}")  # 交換前的值
(a,b)=(b,a)  # 交換a和b的值
print(f"交換後 a={a} b={b}")  # 交換後的值
#%% 交換練習
i=7
j=8
k=9
print(f"交換前 i={i} j={j} k={k}")  # 交換前的值
(i,j,k)=(k,i,j)  # 進行循環交換
print(f"交換後 i={i} j={j} k={k}")  # 交換後的值
#%% tuple to list
tuple1=("kitty",15,"cute")
tuple2=("bb",2025,"aa")
list1=list(tuple1)  # 將元組轉換為串列
list1.append("ff")  # 新增元素到串列
print(list1)
list1[2]=55  # 修改串列中的元素
print(list1)
#%% list to tuple
list1 = ["sofia", "kitty", "apple"]  # 定義串列
print("List:", list1)  # 印出原始串列
tuple1 = tuple(list1)  # 將串列轉換為元組
print("Tuple:", tuple1)  # 印出轉換後的元組
#%% 2D tuple
fruits=(("香蕉",34,2),("芭樂",28,3),("水梨",50,2))  # 二維元組（品名、數量、單價）
print("品名\t\t數量\t\t單價\t\t小計")  # 列表標題
total_price=0
for i in fruits:
    name,count,price=i 
    total_price+=price*count # 計算總價
    print(f"{name}\t\t{count}\t\t{price}\t\t{count*price}")
print(f"總計\t\t\t\t\t\t{total_price}")  # 印出總價
#%% Dict
dictionary={'name':'EliasChen','age':15,'gay':True}  # 建立字典
print(dictionary)  # 印出整個字典
print(dictionary['age'])  # 取得特定鍵的值
dictionary['name']='yikai'  # 修改鍵的值
print(dictionary['name'])  # 印出修改後的值
# del dictionary['name']  # 刪除特定資料
dictionary['love_kitten']=True  # 新增資料
print(dictionary)
# print(dictionary['meow']) # 取得不存在的key（會產生錯誤）
print(dictionary.get("meow"))  # 取得不存在的key（回傳None）
print(dictionary.get("meow","Not Found QQ"))  # 取得不存在的key並設定預設值
print('age' in dictionary)  # 檢查資料是否存在
# del dictionary
# print(dictionary)
#%% Dict convert
list1=[['name','elias'],['age',15],['love_kitten',True]]  # 定義二維串列
dict1=dict(list1)  # 將二維串列轉換為字典
print(list1)
print(dict1)
#%% create dict with fromkeys
dict3=dict.fromkeys(('name','age'),15)  # 使用fromkeys建立字典（所有值相同）
print(dict3)
#%% dict get: keys, values, items
dictionary={'name':'EliasChen','age':15,'gay':True}  # 定義字典
print(dictionary.keys())  # 印出所有鍵
print(dictionary.values())  # 印出所有值
print(dictionary.items())  # 印出所有鍵值對
#%% dict update
dict1={'name':'EliasChen','age':15,'gay':True}
dict2={'fav_animal':'meow','fav_num':10}
print(dict1)
dict1.update(dict2)  # 將字典2的內容合併到字典1
print(dict1)
dict1.clear()  # 清空字典
print(dict1)
#%% dict pratice
def show_res():  # 顯示商品結果的函式
    print(f'貨號:{id} 品名:{data[id][0]} 售價:{data[id][1]}')

data={  # 定義商品字典
    'A001':['汽水',25],
    'A005':['公主麵',10],
    'A006':['口香糖',8],
    'A003':['冰糖',20]      
}
id=input("請輸入貨號: ")  # 輸入要查詢的貨號
if id not in data.keys():  # 若貨號不存在
    print(f'貨號:{id} 不存在')
    name=input("請輸入品名:")  # 輸入新品名
    price=int(input("請輸入售價:"))  # 輸入新售價
    data[id]=[name,price]  # 新增到字典
    print(data)
show_res()  # 顯示結果
#%% dict pratice
people={}  # 初始化空字典
total=int(input("請決定人數: "))  # 輸入人數
for i in range(1,total+1):  # 迴圈輸入每個人的資訊
    name=input(f'請輸入第{i}位姓名: ')  # 輸入姓名
    people[name]=input(f'請輸入第{i}位電話: ')  # 輸入電話
req=input('請輸入要查詢的電話的姓名: ')  # 輸入要查詢的姓名
if req in people:  # 若姓名存在印出電話號碼
    print(f'{req}的電話號碼是{people[req]}')
#%% set
set1={'banana','banana'}  # 建立集合（重複元素會自動去除）
print(set1)  # 印出集合
print(set('banana'))  # 將字串轉換為集合
dict2={'fav_animal':'meow','fav_num':10}  # 定義字典
print(set(dict2))  # 將字典鍵轉換為集合
set1.add('apple')  # 新增元素
set1.add('orange')  # 新增元素
print(set1)
set1.remove('apple')  # 移除元素（若不存在則發生錯誤）
print(set1)
set1.discard("orange") # 移除元素（若不存在則不做任何動作）
print(set1)
set1.update({'meow','kitty'})  # 合併集合
print(set1)
set1.pop()  # 隨機移除一個元素
print(set1)
set1.pop()  # 隨機移除一個元素
print(set1)
#%% 集合應用
g1=['林二','王一','張三','趙六','王一','李四','張三','陳五']  # 有重複的熱門音樂社名單
g2=['鄭十','趙六','劉千','廖八','柯七','張三','王一','呂九','柯七','蔡百']  # 有重複的流行音樂社名單
# 將名單轉換為集合以去除重複成員
pop=set(g2)
hot=set(g1)
print(hot)
print(f"熱門音樂社名單人數:{len(g1)}\t\t正確人數:{len(hot)}\n")  # 比較重複前後的人數
print(pop)
print(f"流行音樂社名單人數:{len(g2)}\t\t正確人數:{len(pop)}\n")  # 比較重複前後的人數
print(f'重複加社名單: {hot&pop}')  # 同時在兩個社團的成員（交集）
merge=hot|pop  # 兩個社團的所有成員（聯集）
print(f'合併後社團名單: {merge}')
print(f'合併後社團人數: {len(merge)}')  # 印出合併後的人數
print(f'只單獨在流行音樂社的名單: {pop-hot}')  # 只在流行音樂社的成員（差集）
print(f'只單獨在熱門音樂社或流行音樂社的名單: {pop^hot}')  # 只在其中一個社團的成員（對稱差集）