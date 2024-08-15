



def sol(num:int):
    
    if (num & (num-1))==0:
        return True
    
    return False


print(sol(13))
print(sol(32))
print(sol(18))