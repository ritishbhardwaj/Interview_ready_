from typing import *
from collections import deque



class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        self.vis=[0 for i in range(V)]

        for node in range(V):
            if self.vis[node]==0:
                if self.dfs_detect(adj,node,parent=-1)==True:
                    return True

        return False

    
    def dfs_detect(self,grapoh,node,parent) -> bool:
        self.vis[node]=1

        for n in grapoh[node]:
            if self.vis[n]!=1 and n!=parent:
                ans=self.dfs_detect(grapoh,n,node)
                # print("--------->",ans)
                if ans==True:
                    return True
            
            elif self.vis[n]==1 and n!=parent:
                return True
        
        return False


        



obj=Solution()
# adj = [[1], [0,2,4], [1,3], [2,4], [1,3]] 
# V=len(adj)
# ans= obj.isCycle(V,adj)
# print(ans)
# adj = [[], [2], [1,3], [2]]
# V=len(adj)
# ans= obj.isCycle(V,adj)
# print(ans)
adj=[[1],[0,2],[1,3],[2,8,4],[3,5],[4,6],[5],[8],[7,3]]
V=len(adj)
ans= obj.isCycle(V,adj)
print(ans)