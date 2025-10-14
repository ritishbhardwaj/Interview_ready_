class Solution:
    def nextLargerElement(self, arr):
        # code here
        ans=[-1]
        st=[arr[-1]]  #monotonic stack
        for i in range(len(arr)-2,-1,-1):
            
            while st and st[-1]<=arr[i]:
                st.pop()
                
            if st : 
                nge=st[-1]
            else: 
                nge=-1
            st.append(arr[i])
            ans.append(nge)
        
        return ans
    

obj=Solution()
arr=[6, 8, 0, 1, 3]
print(obj.nextLargerElement(arr=arr))