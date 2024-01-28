f=open('abc.txt','r')
words=[]
for line in f:
    words=line.split()
word = input('enter the word for count :')
count=0
for x in words:
    if x==word:
        count+=1
print('total count of {} words in a file is {} :'.format(word,count))
