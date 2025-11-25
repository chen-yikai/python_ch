#%% 關係運算
k=10
i='T' > 'C'  # 字元比較
j=((7+i)==k)  # 布林轉數值運算
m=8+(10<55)*3+(30!=89)*4  # 布林當數值使用

print(f"Display as str: i={i} j={j} m={m}")
print(f"Show as int: i={int(i)} j={int(j)} m={int(m)}")  # 布林轉整數

#%% 邏輯運算
a=5
b=9
i=(b==7) and (a>4)  # AND運算
j=(a+b==14) or (b<3)  # OR運算
k=not((a<=b) and (a<b) or ('A' > 'C'))  # NOT運算
print(f"i={i} j={j} k={k}")

#%% if
score=int(input("請輸入成績(0-100): "))
if score >= 60:  # 及格判斷
    print("及格啦~")
if score >= 55 and score < 60:  # 通融範圍
    print("給你通融過關啦~")
if score < 58:  # 不及格判斷
    print("沒救了，就是不及格啦~")

#%% if else
age=int(input("請輸入年齡: "))
if age < 10  or age >= 65:  # 優待票條件
    print("您可購買優待半票")
else:
   print("您須購買一般全票")

#%% 巢狀if else
a=int(input("請輸入第一個正數: "))
b=int(input("請輸入第二個正數: "))
c=int(input("請輸入第三個正數: "))
max_int=0
if a > b:  # 比較a和b
    if a > c:  # a最大時比較a和c
        max_int=a
    else:
        max_int=c
else:
    if b > c:  # b最大時比較b和c
        max_int=b
    else:
        max_int=c
print(f"三數之中最大的是{max_int}")

#%% else if
price=float(input("輸入價格: "))
if price > 100000:  # 價格區間判斷
    price *= 0.8
    print("打8折")
elif price > 50000:
    price *= 0.85
    print("打85折")
elif price > 30000:
    price *= 0.9
    print("打9折")
elif price > 10000:
    price *= 0.95
    print("打95折")
else:
    print("不打折")
print(f"價格為{price:.0f}")