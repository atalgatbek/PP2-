#Write a Python program to copy the contents of a file to another file
import os
import shutil

def copy(f1, f2):
    if os.path.isfile(f1):
        shutil.copyfile(f1, f2)
        print('copied')
    else:
        print('file doesnt exists')
    
f1 = 'C:/Users/talga/OneDrive/Рабочий стол/PP2 Lab/Lab 6/dir-files/7task.txt'
f2 = 'C:/Users/talga/OneDrive/Рабочий стол/PP2 Lab/Lab 6/dir-files/7taskcopy.txt'
copy(f1, f2)