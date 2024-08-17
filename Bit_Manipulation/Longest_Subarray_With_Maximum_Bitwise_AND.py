from typing import *


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        maxii = max(nums)
        max_l = 1
        l=1
        for i in range(1,len(nums)):
           
           if nums[i]!=maxii:
               l=1
               continue
           elif nums[i]==nums[i-1] and nums[i]==maxii:
               l+=1
               max_l=max(max_l,l)
        
        return max_l
                    
    
obj=Solution()
print(obj.longestSubarray([10,2,2,2,3,3,5,5]))
print(obj.longestSubarray(nums = [1,2,3,3,2,2]))
print(obj.longestSubarray(nums = [1,2,3,4]))