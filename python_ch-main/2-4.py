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
#%% 2d tuple
fruits=(("香蕉",34,2),("芭樂",28,3),("水梨",50,2))
print("品名\t\t數量\t\t單價\t\t小計")
total_price=0
for i in fruits:
    name,count,price=i
    total_price+=price*count
    print(f"{name}\t\t{count}\t\t{price}\t\t{count*price}")
print(f"總計\t\t\t\t\t\t{total_price}")