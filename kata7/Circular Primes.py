from itertools import permutations
from math import sqrt

def circular_prime(n):
    prime_string = [str(n)]

    if len(str(n)) <= 1:
        return is_prime(n)

    circular_perms = []
    for j, _ in enumerate(str(n)):
        circular_perms.append(rotate(str(n), j))
        
    return all([ is_prime(int(i)) for i in circular_perms])



def rotate(data,shift):
    first = data[0 : shift]
    second = data[shift :]
    return second + first


def is_prime(n):
    if n < 2:
        return False
    print(n)
    for i in range(2, int(sqrt(n)) +1):
        if n % i == 0:
            break
    else:
        return True
    return False
