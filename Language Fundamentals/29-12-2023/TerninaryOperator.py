a,b=10,20 
x=30 if a<b else 40 
print(x) #30

a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
c=int(input("Enter Third Number:")) 
min=a if a<b and a<c else b if b<c else c   #Nesting terinary operator
print("Minimum Value:",min)
