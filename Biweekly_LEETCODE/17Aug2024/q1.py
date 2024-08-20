from typing import *
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        i=0
        j=k-1
        ans=[]

        while j<len(nums):
            sub = nums[i:j+1]
            prev=sub[0]
            cons=True
            for k in range(1,len(sub)):
                if sub[k]==prev+1:
                    prev=sub[k]
                else:
                    cons=False
            if cons==False:
                ans.append(-1)
            else:
                ans.append(prev)
            
            i+=1
            j+=1
        
        return ans
        
        
o=Solution()
print(o.resultsArray(nums = [2,2,2,2,2], k = 4))