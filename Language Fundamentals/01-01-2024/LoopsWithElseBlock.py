cart=[10,20,30,40,50]
for item in cart:
  if item>=500:
    print("We cannot process this order")
    break
  print(item)
else:
  print("Congrats ...all items processed successfully")
