import os
import pandas as pd
from threading import *
def readTextFile(filepath,encrypt_value):
    data=''
    encrypted_data=''
    f=open(filepath,'r')
    for line in f:
        data=data+str(line) 
    for char in data:
        ascii_value=ord(char)
        if ascii_value>=65 and ascii_value<=90:
            if ascii_value+encrypt_value>90:
                encrypted_data=encrypted_data+chr((ascii_value+encrypt_value)-26)
            else:
                encrypted_data=encrypted_data+chr(ascii_value+encrypt_value)
        else:
            encrypted_data=encrypted_data+char
            
    new_filepath=filepath+'encrypted'
    f=open(new_filepath,'w')
    f.write(encrypted_data)

path = input('Input:')
encrypt_value=int(input('enter the encrypt value :'))
threads=[]
for dirpath,dirnames,filenames in os.walk(path):
    for x in filenames:
        filepath=dirpath+'/'+x
        print(filepath)
        if(filepath.endswith('.txt')):
            t1=Thread(target=readTextFile,args=(filepath,encrypt_value,))
            t1.start()
            threads.append(thread)
for thread in threads:
    thread.join()

print("All threads completed")
