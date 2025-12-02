#%% print基本語法
print("My python journey with TAI\n")  # 印出字串
name="elias"  # 字串變數
age=19        # 整數變數
float_num=0.444  # 浮點數變數
print(name)
print(age)
print(float_num)
print(f"\nmy name is {name}, i'm {age} years old")  # f-string格式化

#%% 算術運算子
length=10
print("圓計算")
print("圓半徑:",length)
print("圓面積:",length**2 * 3.14)  # 計算圓面積
print("圓周長:",round(length * 2 * 3.14,2))  # 計算圓周長
print("圓球體積:",round((4/3)*3.14 * length**3,2))  # 計算球體積

#%% 自動型別轉換
b,i,f = True, 2, 3.4  # 布林、整數、浮點數
print(b+i,b+f,i+f)    # 自動轉換加法
print(b-i,b-f,i-f)    # 自動轉換減法
print(b*i,b*f,i*f)    # 自動轉換乘法

#%% 強制型別轉換
i1=10
f1=float(i1)  # 整數轉浮點數
num=5.544
num_int=int(num)  # 浮點數轉整數
print(i1,f1,type(f1))
print(num,num_int,type(num_int))

numbers=123456
numbers_text=str(numbers)  # 整數轉字串
print(numbers,numbers_text,type(numbers_text))
bool_value=bool(numbers)  # 整數轉布林
print(bool_value)

#%% print函式
print("Python",2.7)  # 多參數
print('Japan','Taiwan','French',sep=',')  # 分隔符號
print("Hsinchu","Taipei",sep='\t\t')  # Tab分隔
print("Price",end=':')  # 結尾字元
price=90
print("hamburger",price,"dollar")

#%% print format 用法
print("%c%s先生"%('張','無忌'))  # 字元與字串格式化
wt,price=30,20.5
print("香蕉%d斤,共%.1f元"%(wt,wt*price))  # 數值格式化

#%% 混合運算
n1=18
n2=7
n3=12.9
t=(n1%n2*21)//2.0**3.0-n2  # 運算優先順序
print(t)

#%% 字串練習
n1="Hello"
n2="World"
strSum=n1+n2  # 字串連接
repeat="hi"
print(strSum)
print(repeat * 10)  # 字串重複

print("\ninput函式")
userName = input("Please enter username: ")  # 取得輸入
age = int(input("Please enter age: "))       # 輸入轉型
print('\nName: %s\tage: %d'%(userName,age))  # 格式化輸出
print(f"\nName: {userName} \tage: {age}")    # f-string輸出