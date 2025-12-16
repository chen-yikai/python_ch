#%% 元組
tuple1=("kitty",15,"cute")
print(tuple1)
a,b,c=tuple1
print(a)
tuple1+=("meow",)
print(tuple1)
print(len(tuple1))
# del(tuple1)
# print(tuple1)
#%% 數值交換
i=10
b=20
c=5
print(f"交換前 a={a} b={b}")
(a,b)=(b,a)
print(f"交換後 a={a} b={b}")
#%% 交換練習
i=7
j=8
k=9
print(f"交換前 i={i} j={j} k={k}")
(i,j,k)=(k,i,j)
print(f"交換後 i={i} j={j} k={k}")
#%% tuple to list
tuple1=("kitty",15,"cute")
tuple2=("bb",2025,"aa")
list1=list(tuple1)
list1.append("ff")
print(list1)
list1[2]=55
print(list1)
#%% list to tuple
list1 = ["sofia", "kitty", "apple"]
print("List:", list1)
tuple1 = tuple(list1)
print("Tuple:", tuple1)
#%% 2D tuple
fruits=(("香蕉",34,2),("芭樂",28,3),("水梨",50,2))
print("品名\t\t數量\t\t單價\t\t小計")
total_price=0
for i in fruits:
    name,count,price=i
    total_price+=price*count
    print(f"{name}\t\t{count}\t\t{price}\t\t{count*price}")
print(f"總計\t\t\t\t\t\t{total_price}")
#%% Dict
dictionary={'name':'EliasChen','age':15,'gay':True}
print(dictionary)
print(dictionary['age'])
dictionary['name']='yikai'
print(dictionary['name'])
del dictionary['name']
print(dictionary)
dictionary['love_kitten']=True
print(dictionary)
# print(dictionary['meow'])
print(dictionary.get("meow"))
print(dictionary.get("meow","Not Found QQ"))
print('age' in dictionary)
# del dictionary
# print(dictionary)
#%% Dict convert
list1=[['name','elias'],['age',15],['love_kitten',True]]
dict1=dict(list1)
print(list1)
print(dict1)
#%% create dict with fromkeys
dict3=dict.fromkeys(('name','age'),15)
print(dict3)
#%% dict get: keys, values, items
dictionary={'name':'EliasChen','age':15,'gay':True}
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
#%% dict update
dict1={'name':'EliasChen','age':15,'gay':True}
dict2={'fav_animal':'meow','fav_num':10}
print(dict1)
dict1.update(dict2)
print(dict1)
dict1.clear()
print(dict1)
#%% dict pratice
def show_res():
    print(f'貨號:{id} 品名:{data[id][0]} 售價:{data[id][1]}')
data={
    'A001':['汽水',25],
    'A005':['公主麵',10],
    'A006':['口香糖',8],
    'A003':['冰糖',20]      
}
id=input("請輸入貨號: ")
if id not in data.keys():
    print(f'貨號:{id} 不存在')
    name=input("請輸入品名:")
    price=int(input("請輸入售價:"))
    data[id]=[name,price]
    print(data)
show_res()
#%% dict pratice
people={}
total=int(input("請決定人數: "))
for i in range(1,total+1):
    name=input(f'請輸入第{i}位姓名: ')
    people[name]=input(f'請輸入第{i}位電話: ')
req=input('請輸入要查詢的電話的姓名: ')
if req in people:
    print(f'{req}的電話號碼是{people[req]}')
#%% set
set1={'banana','banana'}
print(set1)
print(set('banana'))
dict2={'fav_animal':'meow','fav_num':10}
print(set(dict2))
set1.add('apple')
set1.add('orange')
print(set1)
set1.remove('apple')
print(set1)
set1.discard("orange") # include error handling
print(set1)
set1.update({'meow','kitty'})
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
#%% 集合應用
g1=['林二','王一','張三','趙六','王一','李四','張三','陳五']
g2=['鄭十','趙六','劉千','廖八','柯七','張三','王一','呂九','柯七','蔡百']
hot=set(g1)
pop=set(g2)
print(hot)
print(f"熱門音樂社名單人數:{len(g1)}\t\t正確人數:{len(hot)}\n")
print(pop)
print(f"流行音樂社名單人數:{len(g2)}\t\t正確人數:{len(pop)}\n")
print(f'重複加社名單: {hot&pop}')
merge=hot|pop
print(f'合併後社團名單: {merge}')
print(f'合併後社團人數: {len(merge)}')
print(f'只單獨在流行音樂社的名單: {pop-hot}')
print(f'只單獨在熱門音樂社或流行音樂社的名單: {pop^hot}')