# scores=[[27,"Elias",70,80,95,200],[7,"Sofia",40,80,100,200]]
scores=[]  # 學生成績列表
studentCount=int(input("請輸入學生人數: "))  # 讀取人數
print()
tempSearch=""  # 查詢值
tempIndex=0  # 查詢欄位索引
search=False  # 是否查詢模式

for i in range(studentCount):  # 逐位輸入座號/姓名/成績
    number=int(input(f"請輸入第{i+1}位學生座號: "))
    name=input("請輸入姓名: ")
    chinese=int(input("請輸入國文成績: "))
    english=int(input("請輸入英文成績: "))
    math=int(input("請輸入數學成績: "))
    scores.append([number,name,chinese,english,math,chinese+english+math])  # 附帶總分
    print()

def displayScores():  # 顯示表格/平均
    hasResult=False
    for i in scores:
        if tempSearch==str(i[tempIndex]):
            hasResult=True
    if hasResult or not search: print("座號\t\t姓名\t\t國文\t\t英文\t\t數學\t\t總分")
    chineseSum=0  
    englishSum=0  
    mathSum=0 
    totalSum=0 
    searchItemCount=0
    for i in scores:
        sum=i[5]  # 取得該學生的總分
        # 累加各科成績
        chineseSum+=i[2]
        englishSum+=i[3]
        mathSum+=i[4]
        totalSum+=sum  # 累加總分
        if not search or tempSearch==str(i[tempIndex]):  # 若不是查詢或符合查詢條件則顯示
            if search and tempSearch==str(i[tempIndex]):
                searchItemCount+=1
            print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}\t\t{sum}")
    print()
    count=len(scores)  # 總人數
    if search and searchItemCount==0:  # 無查詢結果
        print("查無此資料 ! ....\n")
    if not search:  # 非查詢時列平均
        print(f"平均\t\t\t\t\t{chineseSum/count:.2f}\t{englishSum/count:.2f}\t{mathSum/count:.2f}\t{totalSum/count:.2f}")
    print()


while True:  # 功能選單
    print()
    displayScores()
    tempSearch=""  # 重設查詢條件
    tempIndex=0
    search=False
    opt=int(input("1.依座號遞增排序顯示 2.依總分遞減排序顯示 3.依國文成績遞減排序 4.依英文成績遞減排序 5.依數學成績遞減排序 6.依座號查詢學生成績 7.依姓名查詢學生成績 8.離開(請輸入1~8): "))
    match opt:
        case 1: scores.sort(key=lambda x: x[0])  # 按座號遞增排序
        case 2: scores.sort(key=lambda x: x[5],reverse=True)  # 按總分遞減排序
        case 3: scores.sort(key=lambda x: x[2],reverse=True)  # 按國文成績遞減排序
        case 4: scores.sort(key=lambda x: x[3],reverse=True)  # 按英文成績遞減排序
        case 5: scores.sort(key=lambda x: x[4],reverse=True)  # 按數學成績遞減排序
        case 6:  # 按座號查詢
            tempSearch=input("請輸入要查詢的座號: ")
            tempIndex=0
            search=True
        case 7:  # 按姓名查詢
            tempSearch=input("請輸入要查詢的姓名: ")
            tempIndex=1
            search=True
        case 8: break  # 離開程式