class Solution:
    def resultingString(self, s: str) -> str:

        st=[]

        st.append(s[0])
        for i in range(1,len(s)):
        
            if  st!=[] and ((abs(ord(s[i]) - ord(st[-1])) == 1 ) or (abs(ord(s[i]) - ord(st[-1])) == 25) ) :
                st.pop()
            else:
                st.append(s[i])

        return st
    

obj=Solution()
print(obj.resultingString(s="zadb"))