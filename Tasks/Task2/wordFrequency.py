import os
import pandas as pd
   
#function to read xlsx file
def readXlsxFile(filepath,d):
    df=pd.read_excel(filepath)
    l=df.values.tolist()
    for x in l:
        for y in x:
            if y in d:
                d[y]=d[y]+1
            else:
                d[y]=1

#function to read text file
def readTextFile(filepath,d):
    f=open(filepath,'r')
    words=[]
    for line in f:
        words=line.split()
        for x in words:
            if x in d:
                d[x] = d[x]+1
            else:
                d[x]=1

d=dict()
path = input('Input:')
for dirpath,dirnames,filenames in os.walk(path):
    for x in filenames:
        filepath=dirpath+'/'+x
        print(filepath)
        if(filepath.endswith('.txt')):
            readTextFile(filepath,d)
        elif(filepath.endswith('.xlsx')):
            readXlsxFile(filepath,d)
          
#printing frequency of words
for x in d:
    print(x,':',d[x])


