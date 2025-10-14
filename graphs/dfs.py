from typing import *
from collections import abc,ChainMap,Counter,namedtuple

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        v=len(adj)
        vis=[0 for i in range(v)]
        ans=[]
        def dfs(node):
            nonlocal vis,ans
            
            vis[node]=1
            ans.append(node)
            for i in adj[node]:
                print(i)
                if vis[i]!=1:
                    # vis[i]=1
                    dfs(i)
            
        vis[1]=1  
        dfs(1)
        return ans


if __name__=="__main__":
    
    graph=[[2,3,1], [0], [0,4], [0], [2]]
    graph=[[2, 1], [2, 0], [0, 1]]
    obj=Solution()
    ans= obj.dfsOfGraph(graph)
    print(ans,"  <------")