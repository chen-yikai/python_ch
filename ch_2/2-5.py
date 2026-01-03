# %% os folder
import os # 引入系統模組

path='/ch_1'  # 絕對路徑
if os.path.isdir(path):  # 檢查路徑是否為資料夾
    print(f'{path} folder exist')
else:
    print(f'{path} folder not exist')
    
path='./ch_1'  # 相對路徑（當前目錄）
if os.path.isdir(path):  # 檢查路徑是否為資料夾
    print(f'{path} folder exist')
else:
    print(f'{path} folder not exist')
    
path='../ch_1'  # 相對路徑（上級目錄）
if os.path.isdir(path):  # 檢查路徑是否為資料夾
    print(f'{path} folder exist')
else:
    print(f'{path} folder not exist')
# %% os file
import os

file='2-1.py'  # 指定檔案名稱
if os.path.isfile(file):  # 檢查路徑是否為檔案
    print(f'{file} file exist')
else:
    print(f'{file} file not exist')
#%% os exists
import os

file='C:/Windows/py.exe'  # 指定檔案路徑
if os.path.exists(file):  # 檢查路徑是否存在
    print(f'{file} path exist')
else:
    print(f'{file} path not exist')
#%% os create
import os

path='C:/kitty/'  # 指定要建立的資料夾路徑

if os.path.exists(path):  # 檢查路徑是否已存在
    print(f'{path} is exists, skipping...')
else:
    confirm=input(f'{path} is not exists, create {path}?(y/n) ')  # 詢問是否建立
    if confirm != 'y':  # 若選擇 n 則離開
        exit;
    os.mkdir(path)  # 建立資料夾
    print(f'successfully create {path}')
#%% os remove
import os

path='C:/kitty/'  # 指定要刪除的資料夾路徑

if os.path.exists(path):  # 檢查路徑是否存在
    confirm=input(f'{path} is not exists, delete {path}?(y/n) ')  # 詢問是否刪除
    if confirm != 'y':  # 若選擇 n 則離開
        exit;
    os.rmdir(path)  # 刪除資料夾
    print(f'successfully deleted {path}')
else:
    print(f'{path} is not exists, skipping...')
#%% cwd
import os
print(f"The current work dir is: {os.getcwd()}")  # 顯示工作目錄路徑
#%% create file
f1=open('../kitty.txt','a')  # 開啟或建立檔案
f1.close()  # 關閉檔案 
#%% write file
f2=open('stu.txt','w') # 開啟檔案（若無則建立）
# 寫入資料
f2.write('z, 99, 98\n')
f2.write('j, 97, 96\n')
f2.write('h, 95, 94\n')
f2.close() # 關閉檔案
#%% read file
f3=open('stu.txt','r') # 開啟檔案（唯讀）
str1=f3.read(8) # 讀取前8個字元
print(str1)
print(f3.read()) # 讀取剩餘內容
f3.close() # 關閉檔案
#%% readline
fName='stu.txt'
with open(fName,'r') as f4: # 開啟檔案（唯讀）
    str1=f4.readline() # 讀取一行
    print(str1)
    str2=f4.readline(7) # 讀取前7個字元
    print(f4.read()) # 讀取剩餘內容
#%% readlines
with open('stu.txt','r') as f5: # 開啟檔案（唯讀）
    lst=f5.readlines() # 讀取所有行並存為串列
    print()
    print(lst)
#%% w+ file
fName='stu.txt'
with open(fName,'w+') as f6: # 開啟檔案 (可讀寫)(若無則建立）
    f6.write('a, 93, 92\n')
    f6.write('o, 91, 90\n')
    f6.seek(0) # 指標移動到開頭，因為追加模式一開始會在檔案尾巴
    print(f6.read())
#%% append file
fName='stu.txt'
with open(fName,'a') as f7: # 開啟檔案（追加）
    f7.write('zzz, 89, 88\n')
    f7.write('jjj, 87, 86\n')
with open(fName,'r') as f7: # 開啟檔案（唯讀）
    print(f7.read())
#%% read custom lines
import os
fName='stu.txt'
with open(fName,'a+') as f8: # 開啟檔案（可讀寫並追加）
    f8.seek(0) # 指標移動到開頭，因為追加模式一開始會在檔案尾巴
    str1=f8.readline() # 讀取一行
    print(str1,end='')
    
    str1=f8.readlines() # 讀取剩餘行
    print(str1,end='\n')
    
    for x in str1: # 逐行顯示
        print(x,end='')
os.system('cls') # 清除螢幕 windows-'cls' linux-'clear'