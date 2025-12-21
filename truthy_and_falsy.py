a = [1,2,3,0,"",None,[],[1,2],False,True]
b = [1,2,3,4,5]

print(all(a)) # checks if all elements in the iterable are truthy
print(any(a)) # checks if any element in the iterable is truthy

print(all(b))   
print(any(b))


if all(a):
    print("inventory is full")
elif any(a):
    print("some items are missing")
else:
    print("inventory is empty")