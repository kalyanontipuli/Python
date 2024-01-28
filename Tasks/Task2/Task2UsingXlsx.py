import pandas as pd
word=input('enter the word to count :')
count=0
df=pd.read_excel('book2.xlsx')
l=df.values.tolist()
for x in l:
    for y in x:
        if word==y:
            count+=1
print('the no of times the  word {} repeated is {}'.format(word,count))
