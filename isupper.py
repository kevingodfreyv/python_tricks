# The .isupper() method is the simplest and most "Pythonic" way to check if a single character (or a string) is in uppercase.
# It returns True if all cased characters in the string are uppercase and there is at least one cased character, and False otherwise. 
# It ignores numbers, spaces, and symbols. 
"A".isupper()  # True
"a".isupper()  # False
"1".isupper()  # False
"Hello".isupper()  # False
"HELLO".isupper()  # True
"HELLO WORLD!".isupper()  # True
"hello world!".isupper()  # False
"12345".isupper()  # False      
"".isupper()  # False
