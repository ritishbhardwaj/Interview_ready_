from typing import *

class Solution:
    def previousGreaterElements(self, nums: List[int]) -> List[int]:
        
        st=[]
        ans=[]

        for i in range(len(nums)):

            while st and st[-1]<= nums[i]:
                st.pop()

            if st: pge=st[-1]
            else:
                pge=-1

            ans.append(pge)
            st.append(nums[i])

        return ans       


obj=Solution()
nums = [1,2,3,4,3]  #[-1  -1  -1  -1  4]
print(obj.previousGreaterElements(nums=nums))
nums=[6,0,8,1,3] # [-1 6  -1  8 8]
print(obj.previousGreaterElements(nums=nums))