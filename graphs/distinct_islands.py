
import sys
from typing import List
sys.setrecursionlimit(10**8)
from collections import deque
import heapq

#wrong solution with Heaps

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:


        self.dx=[1,0,-1,0]
        self.dy=[0,1,0,-1]
        self.rows=len(grid)
        self.cols=len(grid[0])

        self.vis=[[0 for i in range(self.cols)] for _ in range(self.rows)]

        self.distict_ds=set()
        for i in range(self.rows):
            for j in range(self.cols):
                temp=[]
                heapq.heapify(temp)
                if self.vis[i][j]!=1 and grid[i][j]==1:
                    self.dfs_count(i,j,temp,grid)
                
                    sub=[]
                    small_r,small_c=heapq.heappop(temp)
                    sub.append((small_r-small_r,small_c-small_c))
                    while temp:
                        other_r,other_c=heapq.heappop(temp)
                        sub.append((abs(other_r-small_r),abs(other_c-small_c)))
                    sub.sort()
                    self.distict_ds.add(tuple(sub))
        # print(self.distict_ds)
        return len(self.distict_ds)


    def dfs_count(self,r,c,ds:heapq,grid):

        self.vis[r][c]=1
        heapq.heappush(ds,(r,c))
        for i in range(4):
            nr=r+self.dx[i]
            nc=c+self.dy[i]

            if nr >=0 and nc>=0 and nr<self.rows and nc <self.cols and self.vis[nr][nc]!=1 and grid[nr][nc]==1 :
                self.dfs_count(nr,nc,ds,grid)




obj=Solution()
grid=[ [1, 1, 0, 1, 1],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1],
       [1, 1, 0, 1, 1]]

ans=obj.countDistinctIslands(grid=grid)
print(ans)



if __name__ == "__main__":
    print(dir(heapq))
    print(help(heapq.nlargest))
    print(help(heapq.nsmallest))