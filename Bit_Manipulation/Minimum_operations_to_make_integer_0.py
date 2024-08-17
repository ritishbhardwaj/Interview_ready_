# print(bin(5))
# print(-21^5)
# print(21^5)
# print(bin(-21))
# print(bin(~(-21)))
# print(bin(20))
# print(-2|5)


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        for step in range(1,36):
            diff = num1 - step*num2

            if diff<0:
                continue
            b = bin(diff)
            bits = b.count("1")
            print(bits,step)
            if bits<= step and diff>=step:
                return step
        
        return -1
    
obj = Solution()
print(obj.makeTheIntegerZero(6,5))