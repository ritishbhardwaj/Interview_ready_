from collections import deque
from typing import *

class Solution:


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        adjL=[]

        for i in range(len(isConnected)):
            sub=[]
            for j in range(len(isConnected[0])):
                if (isConnected[i][j]==1 ):
                    sub.append(j)
            adjL.append(sub)
        
        print(adjL)
        isConnected=adjL[:]
        self.vis=[0 for i in range(len(isConnected))]
        n=0
        for i in range(len(isConnected)):
            if self.vis[i]==0:
                n+=1
                self.dfs(i,isConnected)
        return n

    def dfs(self,node,graph):
        
        self.vis[node]=1

        for adjacent_node in graph[node]:
            if self.vis[adjacent_node]==0:
                self.dfs(adjacent_node,graph)
        


if __name__ == "__main__":
    graph=[[1,1,0],[1,1,0],[0,0,1]]
    graph= [[1,0,0],[0,1,0],[0,0,1]]
    # graph=[[1,1,0],[1,1,0],[0,0,1]]
    obj=Solution()
    ans=obj.findCircleNum(graph)
    print(ans)
