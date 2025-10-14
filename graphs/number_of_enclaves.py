from typing import *
from collections import deque


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        self.n=len(grid)
        self.m=len(grid[0])
        ans=0
        vis=[[0 for _ in range(self.m)] for _ in range(self.n)]

        self.dx=[1,0,-1,0]
        self.dy=[0,1,0,-1]
        for i in range(self.n):
            for j in range(self.m):
                self.flag=0     # this flag will make sure that we exit the boundary
                if vis[i][j]!=1 and grid[i][j]==1:
                    total=self.bfs(i,j,grid,vis)
                    if self.flag==0:
                        ans+=total

        return ans
                


    def bfs(self,r,c,grid,vis):

        q=deque([])
        q.append((r,c))
        vis[r][c]=1
        n=1
        while q:
            r,c=q.popleft()

            for dir in range(4):
                nr=r+self.dx[dir]
                nc=c+self.dy[dir]

                if nr>=0 and nc>=0 and nr<self.n and nc<self.m and vis[nr][nc]!=1 and grid[nr][nc]==1:
                    q.append((nr,nc))
                    n+=1
                    vis[nr][nc]=1
                if nr<0 or nc<0 or nr>=self.n or nc>=self.m :
                    self.flag=1
        return n



obj=Solution()
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
ans=obj.numEnclaves(grid)
print(ans)
grid = [[0],[1],[1],[0],[0]]
ans=obj.numEnclaves(grid)
print(ans)

