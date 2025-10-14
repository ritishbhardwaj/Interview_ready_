from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        self.vis=[0 for i in range(V)]
        
        for i in range(V):
            if self.vis[i]!=1:
                if self.bfs_detect(adj,i,parent=-1) == True :  #initially parent is -1
                    return True
            
        return False
		        
	

    def bfs_detect(self,graph,node,parent:int):
        #configuration
        q=deque([(node,parent)])

        while q:
            full_node=q.popleft()
            node=full_node[0]
            parent=full_node[1]

            for n in graph[node]:
                if self.vis[n]!=1 and n!=parent:
                    self.vis[n]=1
                    q.append((n,node))

                elif self.vis[n]==1 and n!=parent:
                    return True
                

        return False

		
		


	

obj=Solution()
adj = [[1], [0,2,4], [1,3], [2,4], [1,3]] 
V=len(adj)
ans= obj.isCycle(V,adj)
print(ans)
adj = [[], [2], [1,3], [2]]
V=len(adj)
ans= obj.isCycle(V,adj)
print(ans)
