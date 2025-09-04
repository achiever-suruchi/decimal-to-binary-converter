import math

val = float(input("Enter the number to convert: "))
frac, intgr = math.modf(val)

def iconv(i):
    '''Converts integer part to binary and returns binary string'''
    a = ""
    while i != 0:
        a += str(i % 2)
        i //= 2
    return a[::-1] or "0"   # in case i = 0

def fconv(f, precision=10):
    '''Converts fractional part to binary and returns binary string'''
    s = ""
    count = 0
    while f != 0.0 and count < precision:
        f *= 2
        f, b = math.modf(f)
        s += str(int(b))
        count += 1
    return s or "0"   # in case f = 0

print("The binary conversion of", val, "is", iconv(int(intgr)) + "." + fconv(frac, precision=15))
