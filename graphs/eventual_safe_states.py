from typing import *
import heapq

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        

        tn=[] # terminal nodes
        sn=[] #safe nodes
        vis=[0 for i in range(len(graph))]
        path_vis=[0 for i in range(len(graph))]

        def dfs(node):
            nonlocal vis,path_vis,tn, sn

            vis[node]=1
            path_vis[node]=1
            
            for n in graph[node]:
                if vis[n]==0:
                    if dfs(n)==False:
                        return False
                elif vis[n]==1 and path_vis[n]==1:
                    return False
            
            sn.append(node)
            path_vis[node]=0

        
        for i in range(len(graph)):
            if graph[i]==[]:
                tn.append(i)

        for i in range(len(graph)):
            if vis[i]==0 :
                dfs(i)
            
        # print(sn)
        heapq.heapify(sn)
        return sn


if __name__=='__main__':
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    obj=Solution()
    ans=obj.eventualSafeNodes(graph=graph)
    print(ans)

    graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    ans=obj.eventualSafeNodes(graph=graph)
    print(ans)
