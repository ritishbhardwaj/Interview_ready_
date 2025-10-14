from typing import *
from collections import deque,defaultdict


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n=len(board)
        m=len(board[0])

        vis=[[0 for _ in range(m)] for j in range(n)]

        self.dx=[1,0,-1,0]
        self.dy=[0,1,0,-1]
        for i in range(n):
            for j in range(m):
                if (i==0 or i==n-1 or j==0 or j==m-1 ) and vis[i][j]==0 and board[i][j]=='O':
                    self.dfs(i,j,board,n,m,vis)

        for i in range(n):
            for j in range(m):
                if vis[i][j]!=1 and board[i][j]=="O":
                    board[i][j]="X"
        


        
    def dfs(self,r,c,board,n,m,vis):

        vis[r][c]=1

        for i in range(4):
            nr=r+self.dx[i]
            nc=c+self.dy[i]

            if nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc]==0 and board[nr][nc]=="O":
                self.dfs(nr,nc,board,n,m,vis)        


obj=Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
ans=obj.solve(board=board)
print(board)


test_cases = [
    # Test Case 1: Simple surrounded region
    [["X", "X", "X", "X"],
     ["X", "O", "O", "X"],
     ["X", "X", "O", "X"],
     ["X", "O", "X", "X"]],

    # Test Case 2: Single element board
    [["X"]],

    # Test Case 3: All 'O's on the border (nothing should be changed)
    [["O", "O", "O", "O"],
     ["O", "X", "X", "O"],
     ["O", "X", "X", "O"],
     ["O", "O", "O", "O"]],

    # Test Case 4: Entire board filled with 'O's (only the inner ones should be flipped)
    [["O", "O", "O", "O", "O"],
     ["O", "X", "X", "X", "O"],
     ["O", "X", "O", "X", "O"],
     ["O", "X", "X", "X", "O"],
     ["O", "O", "O", "O", "O"]],

    # Test Case 5: Entire board filled with 'X's (nothing should be changed)
    [["X", "X", "X", "X"],
     ["X", "X", "X", "X"],
     ["X", "X", "X", "X"],
     ["X", "X", "X", "X"]],

    # Test Case 6: Checkerboard pattern
    [["X", "O", "X", "O"],
     ["O", "X", "O", "X"],
     ["X", "O", "X", "O"],
     ["O", "X", "O", "X"]],

    # Test Case 7: Large surrounded region
    [["X", "X", "X", "X", "X"],
     ["X", "O", "O", "O", "X"],
     ["X", "O", "X", "O", "X"],
     ["X", "O", "O", "O", "X"],
     ["X", "X", "X", "X", "X"]],

    # Test Case 8: Multiple disjoint surrounded regions
    [["X", "X", "X", "X", "X"],
     ["X", "O", "X", "O", "X"],
     ["X", "X", "O", "X", "X"],
     ["X", "O", "X", "O", "X"],
     ["X", "X", "X", "X", "X"]],

    # Test Case 9: Complex region with escape routes
    [["X", "X", "X", "X", "X", "X"],
     ["X", "O", "X", "O", "O", "X"],
     ["X", "X", "O", "X", "X", "X"],
     ["X", "O", "X", "O", "X", "X"],
     ["X", "X", "X", "X", "X", "X"]],

    # Test Case 10: Large board with only one 'O' inside surrounded by 'X'
    [["X", "X", "X", "X", "X"],
     ["X", "X", "O", "X", "X"],
     ["X", "X", "X", "X", "X"]]
]
for case in test_cases:
    # obj = Solution()
    obj.solve(case)  # Assuming `solve` modifies the board in place
    print(case)
