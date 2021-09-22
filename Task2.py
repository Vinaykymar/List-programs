#Python Program to Find the Second Largest Number in a List
x = [1,2,4,5,7,9,10,11,12,15,18,19,20]
y = set(x)
y.remove(max(x))
print("After removing first largest num in a list:",y)
max(y)
print("Second largest num in list:",max(y))
