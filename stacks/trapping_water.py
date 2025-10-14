from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max=[height[0]]
        suffix_max=[height[-1]]
        for i in range(1,len(height)):
            j=len(height)-1-i
            if prefix_max[i-1]>=height[i]:
                prefix_max.append(prefix_max[i-1])
            else:
                prefix_max.append(height[i])

            if suffix_max[-1]>=height[j]:
                suffix_max.append(suffix_max[-1])
            else:
                suffix_max.append(height[j])    
        suffix_max=suffix_max[::-1]
        totalW=0
        for i in range(len(height)):
            totalW= totalW +(abs(min(prefix_max[i],suffix_max[i])-height[i]))
        

        return totalW


obj=Solution()
print(obj.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
