


def helper(n:int)->int:
    if n%4==1:
        return 1
    elif n%4==2:
        return n+1
    elif n%4==3:
        return 0
    elif n%4==0:
        return n
    

def sol(l,r):
    l_xor = helper(l-1)
    r_xor= helper(r)
    print(l_xor,r_xor)
    return l_xor ^ r_xor


print(sol(4,8))