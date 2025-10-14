from typing import *
from collections import deque
from copy import deepcopy

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        self.graph = deepcopy(image)
        self.dir_r=[0,1,0,-1]
        self.dir_c=[1,0,-1,0]
        self.q=deque([])
        self.initial_color=color
        self.n=len(image)
        self.m=len(image[0])
        self.vis=[[0 for _ in range(self.m)] for _ in range(self.n)]
        self.dfs_solution((sr,sc),color)
        print(self.graph)

        n=len(image)
        m=len(image[0])

        vis=[[0 for _ in range(m)] for _ in range(n)]

        q=deque([])
        initial_color=image[sr][sc]
        vis[sr][sc]=1
        image[sr][sc]=color
        q.append((sr,sc))
        dir_r=[0,1,0,-1]
        dir_c=[1,0,-1,0]
        while q:
            node=q.popleft()
            r=node[0]
            c=node[1]

            for i in range(4):
                nr=r+dir_r[i]
                nc=c+dir_c[i]

                if nr<n and nc<m and nr>=0 and nc>=0 and vis[nr][nc]==0 and image[nr][nc]==initial_color:
                    vis[nr][nc]=1
                    image[nr][nc]=color
                    q.append((nr,nc))
        
        return image


    def dfs_solution(self,node,color):
        i=node[0]
        j=node[1]
        self.vis[i][j]=1
        self.graph[i][j]=color

        for k in range(4):
            nr=i+self.dir_r[k]
            nc=j+self.dir_c[k]

            if nr<self.n and nc < self.m and nr >=0 and nc >=0 and self.vis[nr][nc]==0 and self.graph[nr][nc]==self.initial_color:
                self.dfs_solution((nr,nc),color)



    # def bfs(self,graph,q)


obj=Solution()
ans= obj.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
print(ans)
ans=obj.floodFill(image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0)
print(ans)