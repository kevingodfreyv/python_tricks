#str.islower() Returns True if all cased characters in the string are lowercase and there is at least one cased character, otherwise False.
print("a".islower())  # True
print("A".islower())  # False
print("1".islower())  # False
print("hello".islower())  # True
print("Hello".islower())  # False
print("hello world!".islower())  # True
print("HELLO WORLD!".islower())  # False
print("12345".islower())  # False
print("".islower())  # False
print("hello123".islower())  # True
print("hello_world".islower())  # True
print("hello World".islower())  # False
print("hello-world".islower())  # True
print("hello.world".islower())  # True
print("hello\nworld".islower())  # True