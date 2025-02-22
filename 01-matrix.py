# Time: O(m*n)
# Space: O(n*m)
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dq = deque()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: dq.append((i,j))
                elif mat[i][j] == 1: mat[i][j] = -1

        while(len(dq) > 0):
            (i, j) = dq.popleft()
            for u, v in directions:
                nr = i+u
                nc = j+v
                if nr >= 0 and nr < m and nc >= 0 and nc < n and mat[nr][nc] == -1: 
                    mat[nr][nc] = mat[i][j] + 1
                    dq.append((nr,nc))
        return mat

