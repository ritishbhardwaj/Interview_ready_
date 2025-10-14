from typing import *
from collections import deque

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        nse_ind=[len(arr)]*(len(arr)-1)
        st_nse=[(arr[-1],len(arr)-1,len(arr))]   #(ele,ind)
        pse_ind=deque([-1])
        st_pse=[(arr[0],0)]

        #to get nse
        for i in range(len(arr)-2,-1,-1):
            while st_nse and arr[i]<=st_nse[-1][0]:
                st_nse.pop()

            if st_nse:
                ele,ind=st_nse[-1][0],st_nse[-1][1]

            st_nse.append((ele,ind))
            nse_ind.append(ind)
        nse_ind.reverse()
        print(nse_ind)

        #to get pse
        for i in range(1,len(arr)):

            while st_pse and arr[i]<=st_pse[-1][0]:
                st_pse.pop()

            if st_pse:
                ele,ind=st_pse[-1][0],st_pse[-1][1]
            else:
                ele,ind=arr[i],-1
            pse_ind.append(ind)
            st_pse.append((ele,ind))
        
        print(pse_ind)

        summ=0
        for i in range(len(arr)):
            left_subarrays=abs(i-pse_ind[i])
            right=abs(nse_ind[i]-i)
            summ =summ+ (left_subarrays*right*arr[i])

        return summ


obj=Solution()
# print(obj.sumSubarrayMins(arr = [11,81,94,43,3]))
# print(obj.sumSubarrayMins(arr = [3,1,2,4]))

arr = [3,1,2,4]
print(id(arr[0])==id(arr[1]))