from typing import *
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        i=0
        j=k-1
        ans=[]
        other =[1]
        #initial steps
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                other.append(1)
            else:
                other.append(-1)
        
        for i in range(k-1,len(nums)):
            if -1 in other[i-k:i+1]:
                ans.append(-1)
            else:
                ans.append(nums[i])
            
        
        return ans
    
    
o=Solution()
# print(o.resultsArray(nums = [1,2,3,4,3,2,5], k = 3))
# print(o.resultsArray( nums = [2,2,2,2,2], k = 4))
print(o.resultsArray( nums = [3,2,3,2,3,2], k = 2))