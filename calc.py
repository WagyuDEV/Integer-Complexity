import math
from enum import Enum

# anything less than 4 is assumed to be prime, including 1 and 0
def isPrime(n):
    if n <= 3:
        return True
    for i in range(2,10):
        if(n % i == 0 and n != i):
            return False
    return True

class Comp(Enum):
    ZERO=0
    ONE=1
    TWO=2
    THREE=3
    FOUR=4
    FIVE=5
    SIX=5
    SEVEN=6
    EIGHT=6
    NINE=6

def compHandle(n):
    if n == 0:
        return Comp.ZERO.value
    elif n == 1:
        return Comp.ONE.value
    elif n == 2:
        return Comp.TWO.value
    elif n == 3:
        return Comp.THREE.value
    elif n == 4:
        return Comp.FOUR.value
    elif n == 5:
        return Comp.FIVE.value
    elif n == 6:
        return Comp.SIX.value
    elif n == 7:
        return Comp.SEVEN.value
    elif n == 8:
        return Comp.EIGHT.value
    elif n == 9:
        return Comp.NINE.value

# n must be larger than 3 and not prime otherwise [0,0] is returned
def leastFactors(n):
    f1 = 0
    f2 = 0

    if n <= 3:
        return [0, 0]
    if isPrime(n):
        return [0, 0]
    for f in range(2,10):
        if n % f == 0:
            f1 = f
            break
    for f in range(f1, n):
        if f * f1 == n:
            f2 = f
            break
    return [f1, f2]

# TODO: make recursive 
def complexity(n):
    roots = []
    p = False

    if n <= 9:
        return compHandle(n)

    if not isPrime(n):
        while True:
            f = leastFactors(n)
            roots.append(f[0])
            if isPrime(f[1]):
                roots.append(f[1])
                break
            else:
                n = f[1]
    else:
        n = n-1
        p = True
        while True:
            f = leastFactors(n)
            roots.append(f[0])
            if isPrime(f[1]) and f[1] <= 9:
                roots.append(f[1])
                break
            elif isPrime(f[1]):
                # TODO: handle double digit factors
                # NOT REAL RETURN
                # THIS CODE IS BROKEN
                return 0
            else:
                n = f[1]

    totalComplexity = 0

    for i in range(len(roots)):
        totalComplexity = totalComplexity + compHandle(roots[i])
    if p:
        totalComplexity = totalComplexity+1

    return totalComplexity
    # return roots

n = 23
print(n, complexity(n))

# for i in range(100):
#     print(i, complexity(i))

# for i in range(100):
#     print(i, isPrime(i))

# for i in range(100):
#     print(i, leastFactors(i))