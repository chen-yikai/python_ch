#%% array
list1=["meow",10,True,0.555]  # 混合資料的串列示例
print(list1[0])  # 第一個元素
list1[0]=19  # 修改元素值
print(list1[1])  # 第二個元素
print(list1[-1])  # 最後一個元素
for i in list1:
    print(i)  # 逐一輸出
#%% user input
length=int(input("請輸入資料個數: "))  # 讀取資料筆數
nums=[]
for i in range(length):  # 逐筆輸入資料
    current_input=int(input(f"請輸入第{i+1}個: "))
    nums.append(current_input)
print("你輸入的值依序為: ",end="")
nums_sum=0
for i in nums:  # 累加並顯示
    nums_sum+=i
    print(i,end="\t")
avg=nums_sum/length  # 取得平均
print(f"\n此串列數值總合為: {nums_sum}")
print(f"此串列數值平均為: {avg:.2f}")
print(f"串列中最大值{max(nums)}，最小值為{min(nums)}")
print("此字串資料由大到小排序後: ",end="")
nums.sort(reverse=True)  # 由大到小排序
for i in nums:
    print(i,end="\t")
#%% 二維陣列
list=[["Elias",15],["Kitty",5],["Bunny",2]]  # 巢狀串列
list1=["meow",10,True,0.555]
print(list[1])  # 第二列
print(list[2][1])  # 第三列的第二個值
print()
# 取得長度
print(len(list))
print(len(list1))