
# Approach 1


def sol1(l:list)->int:
    ans=0
    for bitIndex in range(32):
        cnt=0
        
        for i in range(len(l)):
            if (l[i]&(1<<bitIndex)):
                cnt+=1
        
        if cnt%3==1:
            ans=ans|(1<<bitIndex)
    
    return ans

print(sol1([5,5,5,-2,1,1,1,3,3,3]))