from typing import *


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        #doing xor of all elements in array
        x = 0
        for i in range(len(nums)):
            x  = x^nums[i]
        
        for i in range(32):
            
            #checking the bit in number k is set or not
            k_bit_set = k &(1<<i)
            x_bit_set = x &(1<<i)
            
            if k_bit_set != x_bit_set:
                operations+=1
        
        return operations

    

obj= Solution()
print(obj.minOperations([2,1,3,4],1))
print(obj.minOperations([9,12,6,17],5))