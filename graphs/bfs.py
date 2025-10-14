from collections import deque
from typing import *

class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: list[list[int]]) -> list[int]:
        
        
        print(adj)
        q= deque([])
        q.append(adj[0])
        v=len(adj)
        vis= [ 0 for i in range(v)]
        vis[0]=1
        ans=[]
        ans.append(0)
        print(q)
        while q:
            l=q.popleft()
            sub=[]
            for i in l:
                print(i)
                if vis[i]!=1:
                    q.append(adj[i])
                    # sub.append(adj[i])
                    ans.append(i)
                    vis[i]=1
            print(q)
        
        print(type(ans))
        return ans
        
        # expected [0,2,3,1,4]


if __name__=="__main__":
    
    graph=[[2,3,1], [0], [0,4], [0], [2]]
    graph=[[2, 1], [2, 0], [0, 1]]
    obj=Solution()
    ans= obj.bfsOfGraph(graph)
    print(ans,"  <------")