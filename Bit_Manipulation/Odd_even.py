


def sol(n:int):
    
    new_n = n|1
    if new_n==n:
        return "odd"
    
    return "even"


print(sol(10))
print(sol(11))