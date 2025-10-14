from collections import *
from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for oi in range(numCourses)]

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        indegree=[0 for i in range(len(adj))]
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

            for n in adj[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)

        return ans if len(ans)==numCourses else []
        

obj=Solution()
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
ans=obj.findOrder(numCourses,prerequisites)
# print(ans)
numCourses = 2
prerequisites = [[1,0]]
ans=obj.findOrder(numCourses,prerequisites)
print(ans)
numCourses = 2
prerequisites = [[1,0],[0,1]]
ans=obj.findOrder(numCourses,prerequisites)
print(ans)
numCourses,prerequisites=3,[[1,0],[1,2],[0,1]]
ans=obj.findOrder(numCourses,prerequisites)
print(ans)