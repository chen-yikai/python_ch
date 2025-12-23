# %% os folder
import os

path='/ch_1'
if os.path.isdir(path):
    print(f'{path} folder exist')
else:
    print('{path} folder not exist')
    
path='./ch_1'
if os.path.isdir(path):
    print('{path} folder exist')
else:
    print('{path} folder not exist')
    
path='../ch_1'
if os.path.isdir(path):
    print('{path} folder exist')
else:
    print('{path} folder not exist')
# %% os file
import os

file='2-1.py'
if os.path.isfile(file):
    print(f'{file} file exist')
else:
    print(f'{file} file not exist')
#%% os exists
import os
file='C:/Windows/py.exe'
if os.path.exists(file):
    print(f'{file} path exist')
else:
    print(f'{file} path not exist')
#%% os create 
import os
path='C:/kitty/'

if os.path.exists(path):
    print(f'{path} is exists, skipping...')
else:
    confirm=input(f'{path} is not exists, create {path}?(y/n) ')
    if confirm != 'y': exit;
    os.mkdir(path)
    print(f'successfully create {path}')
#%% os remove
import os
path='C:/kitty/'

if os.path.exists(path):
    confirm=input(f'{path} is not exists, delete {path}?(y/n) ')
    if confirm != 'y': exit;
    os.rmdir(path)
    print(f'successfully deleted {path}')
else:
    print(f'{path} is not exists, skipping...')
#%% cwd
import os
print(f"The current work dir is: {os.getcwd()}")
#%% create file
f1=open('../kitty.txt','a')
f1.close()
##%% 