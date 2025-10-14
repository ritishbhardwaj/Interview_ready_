from typing import *
from collections import deque,defaultdict

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.n=len(mat)
        self.m=len(mat[0])
        q=deque([])
        vis=[[0 for _ in range(self.m)] for _ in range(self.n)]
        dist_ans=[[0 for _ in range(self.m)] for _ in range(self.n)]
        d=defaultdict(int)
        for i in range(self.n): 
            for j in range(self.m):
                if mat[i][j]==0 :
                    vis[i][j]=1
                    d[(i,j)]=0
                    q.append((i,j))
        print(d)
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        while q:
            r,c= q.popleft()
            dist=d[(r,c)]
            dist_ans[r][c]=d[(r,c)]


            for i in range(4):
                nr=r+dx[i]
                nc=c+dy[i]

                if nr>=0 and nc>=0 and nr<self.n and nc<self.m and vis[nr][nc]!=1: 
                    q.append((nr,nc))
                    d[(nr,nc)]=dist+1
                    vis[nr][nc]=1

        return dist_ans


obj=Solution()
mat = [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
ans=obj.updateMatrix(mat)
print(ans)
mat = [[0,0,0],[0,1,0],[1,1,1]]
ans=obj.updateMatrix(mat)
print(ans)

test_cases = [
    # Test Case 1: Large grid with scattered ones
    [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]],
    
    # Test Case 2: Single row with alternating ones and zeros
    [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]],

    # Test Case 3: Single column with multiple ones in between
    [[0], [1], [1], [1], [1], [0]],

    # Test Case 4: All ones except corners are zeros
    [[0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 0]],

    # Test Case 5: Large grid with a diagonal pattern of zeros
    [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]],

    # Test Case 6: Checkerboard pattern of 0s and 1s
    [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]],

    # Test Case 7: Large grid with a plus pattern of zeros
    [[1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]],

    # Test Case 8: Large grid with all ones except a single zero in the center
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],

    # Test Case 9: Long vertical line of zeros in the middle of a large matrix
    [[1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]],

    # Test Case 10: Sparse zeros in a larger matrix
    [[1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]]
]
for case in test_cases:
    obj2 = Solution()
    print(obj2.updateMatrix(case))