from typing import *

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        gtele=-1
        ans=[]
        st=[]
        
        for i in range((len(nums)*2)-1,-1,-1):

            while st and st[-1]<=nums[i%len(nums)]:
                st.pop()

            # if i<len(nums):
            if st : nge=st[-1]
            else:
                nge=-1
            ans.append(nge)
            st.append(nums[i%len(nums)])
        
        return ans[-1:len(nums)-1:-1]   


obj=Solution()
nums = [1,2,3,4,3]
print(obj.nextGreaterElements(nums=nums))