# Python Project
# Write a python program that builds a list of all files on your computer.

import os

path = "C:\\Users\\Ritik Singh"  #starting folder fath
file_list = []

for root, folders, files in os.walk(path):
    for name in files:
        full_name = root + "/" + name
        file_list.append(full_name)
for f in all_files:
    print(f)

print("Total number of files are:", len(file_list))
