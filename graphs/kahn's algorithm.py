from collections import deque

from typing import *


class Solution:
    
    def topologicalSort(self,adj):
        # Code here
        indegree=[0 for i in range(len(adj))]
        vis=[0 for i in range(len(adj))]
        ans=[]

        for i in range(len(adj)):
            for j in range(len(adj[i])):
                indegree[adj[i][j]]+=1

        q=deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.popleft()
            ans.append(node)

            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)

        return ans    


graph= [[],[],[3],[1],[0,1],[2,0]]
obj=Solution()
ans=obj.topologicalSort(graph)
print(ans)