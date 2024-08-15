

def isPowerOfTwo( n: int) -> bool:

        if (n & (n-1)) !=0:
            return False
        return True


print(isPowerOfTwo(16))
print(isPowerOfTwo(20))
print(isPowerOfTwo(21))