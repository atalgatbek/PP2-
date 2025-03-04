#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

if os.path.exists("C:/Users/talga/OneDrive/Рабочий стол/PP2 Lab/Lab 6/dir-files/abu.txt"):
    os.remove("C:/Users/talga/OneDrive/Рабочий стол/PP2 Lab/Lab 6/dir-files/abu.txt")