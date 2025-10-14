
from collections import deque
from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        # code here

        vis=[0 for i in range(len(adj))]
        indegree=[0 for i in range(len(adj))]
        ans=[]

        for i in range(len(adj)):
            for j in range(len(adj[i])):
                indegree[adj[i][j]]+=1

        q=deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        print(q,indegree)
        while q:
            
            node=q.popleft()
            ans.append(node)

            for n in adj[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        print(ans)
        return len(ans)!=len(adj)


obj=Solution()
graph= [[],[],[3],[1],[0,1],[2,0]]
graph=[[],[3,0],[1],[2],[2]]
ans=obj.isCyclic(graph)
print(ans)
