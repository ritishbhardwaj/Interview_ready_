

def sol(n,d):

    sign=True   #means both numerator and denominator are positive and my result would be positive
    
    if n<0 and d>0:
        sign=False
    elif n>0 and d<0:
        sign=False
        
    n=abs(n)
    d=abs(d)
    
    ans=0
    
    while n>=d:
        cnt=0
        x=0
        while ((d<<cnt)<=n):
            cnt+=1
        # cnt=(1<<x-1)
        ans+=(1<<cnt-1)
        n-= d*(1<<cnt-1)
    
    print(2**31)
    
    if ans == 2**31:
        print("hiii")
        return 2**31-1
    
    return ans if sign else -ans


dividend= 1   #numerator
divisor = -1  #denominator

print(sol(dividend,divisor))