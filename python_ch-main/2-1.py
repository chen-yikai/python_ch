#%% array
list1=["meow",10,True,0.555]
print(list1[0])
list1[0]=19
print(list1[1])
print(list1[-1])
for i in list1:
    print(i)
#%% user input
length=int(input("請輸入資料個數: "))
nums=[]
for i in range(length):
    current_input=int(input(f"請輸入第{i+1}個: "))
    nums.append(current_input)
print("你輸入的值依序為: ",end="")
nums_sum=0
for i in nums:
    nums_sum+=i
    print(i,end="\t")
avg=nums_sum/length
print(f"\n此串列數值總合為: {nums_sum}")
print(f"此串列數值平均為: {avg:.2f}")
print(f"串列中最大值{max(nums)}，最小值為{min(nums)}")
print("此字串資料由大到小排序後: ",end="")
nums.sort(reverse=True)
for i in nums:
    print(i,end="\t")
#%% 二維陣列
list=[["Elias",15],["Kitty",5],["Bunny",2]]
list1=["meow",10,True,0.555]
print(list[1])
print(list[2][1])
print()
print(len(list))
print(len(list1))