


def sol(num:int):
    
    print(f"binary of num is : {bin(num)[2:]}")
    
    cnt=0
    
    while num>1:
        rem = num%2
        num = num//2
        if rem ==1 :
            cnt+=1
        
    if num==1:
        cnt+=1
    nn=19
    print(bin(nn))
    print(nn | 1)
    print(bin(nn|1))
    return cnt



print(sol(13))
print(sol(16))
print(sol(163))