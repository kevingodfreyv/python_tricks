arr = list(range(0,100)) # range gets converted to list


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True;

prime_nums = filter(is_prime, arr)# filter function returns an array of elements, which gave an output of True via filter function 
print(list(prime_nums))