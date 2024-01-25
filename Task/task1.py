import os
path = input('Input:')
for dirpath,dirnames,filenames in os.walk(path):
    for x in filenames:
        print(dirpath,x,sep='/')
