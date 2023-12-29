a=10 
b=10 
print(a is b) #True 
x=True 
y=True 
print( x is y) #True

list1=["one","two","three"] 
list2=["one","two","three"] 
print(id(list1)) 
print(id(list2)) 
print(list1 is list2) #False 
print(list1 is not list2) #True 
print(list1 == list2) #True
