import math
from enum import Enum
import matplotlib.pyplot as plt

# anything less than 4 is assumed to be prime, including 1 and 0
def isPrime(n):
    if n <= 3:
        return True
    for i in range(2,10):
        if(n % i == 0 and n != i):
            return False
    return True

def isOdd(n):
    return False if n % 2 == 0 else True

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
    if n <= 0:
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


def complexity(n, a=0):
    if n <= 9:
        return compHandle(n)+a
    
    if not isOdd(n):
        f = leastFactors(n)
        if f[1] <= 9:
            return compHandle(f[0])+compHandle(f[1])+a
        else:
            return complexity(f[1],a)+a
    else:
        return complexity(n-1,a+1)+a

vals = []

for i in range(1000):
    # print(i, complexity(i))
    plt.plot(i, complexity(i), "ro")

# plt.show()
plt.savefig("dist.png")