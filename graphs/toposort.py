from typing import *


class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        # Code here
        st=[]
        vis=[0 for i in range(len(adj))]

        def dfs(node):
            nonlocal vis,st
            vis[node]=1

            for n in adj[node]:
                if vis[n]==0:
                    dfs(n)

            st.append(node)      

        for i in range(len(adj)):
            if vis[i]==0:
                dfs(i)
        
        return st[::-1]


graph= [[1,3],[4],[3],[4],[]]
obj=Solution()
ans=obj.topologicalSort(graph)
print(ans)