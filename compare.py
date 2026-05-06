

arr = [2,3,1,5,6,4,7]

print(sorted(arr))

from functools import cmp_to_key

def compare(n1 , n2):
    if(n1 > n2):
        return -1
    elif(n2 > n1):
        return 1
    else:
        return 0

print(sorted(arr, key = cmp_to_key(compare)))