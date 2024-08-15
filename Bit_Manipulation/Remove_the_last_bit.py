



def sol(n : int):
    print()
    print(f"Original number in binary {bin(n)[2:]}")
    res= n & (n-1)
    return (f"After removing the last set bit {bin(res)[2:]}")


print(sol(84))
print(sol(56))