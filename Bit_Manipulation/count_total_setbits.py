# O(nlogn)

def sol(n:int) ->int:
    total_cnt = 0
    for i in range(1,n+1):
        total_cnt += cnt_bits(i)
    
    return total_cnt



def cnt_bits(num:int) -> int:
    cnt=0
    while num!=0:
        cnt+=num&1
        num = num>>1
        
    return cnt



# print(sol(4))
print(sol(10))



# O(n)


def sol1(num:int ):
    
    ds = dict()
    cnt = 1
    ds[1]=1
    
    for i in range(2,num+1):
        if i&1==0:    #condition of even
            find= i>>1
            cnt += ds[find]
            ds[i] = ds.get(find,0)
            # ds.pop(find)
        else:    #condition of odd
            find = i>>1
            cnt+=ds[find]+1
            ds[i]=ds.get(find,0)+1
            ds.pop(find)
    
    return cnt
            


print(sol1(2000000))