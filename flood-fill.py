# Time: O(m*n)
# Space: O(m*n)
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color: return image
        n = len(image[0])
        m = len(image)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        #BFS
        dq = deque()
        dq.append((sr, sc))
        image[sr][sc] = color
        while len(dq) > 0:
            (r, c) = dq.popleft()
            for (u, v) in directions:
                adj_r = r+u
                adj_c = c+v
                if -1 < adj_r < m and -1 < adj_c < n and image[adj_r][adj_c] == old_color:
                    image[adj_r][adj_c] = color
                    dq.append((adj_r, adj_c))
        return image
    
# Time O(nm)
# Space O(nm) recursion stack space
from collections import deque
class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.n = 0
        self.m = 0

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == color: return image
        self.n = len(image[0])
        self.m = len(image)
        #DFS
        self.dfs(image, sr, sc, color, old_color)
        return image

    def dfs(self, image: List[List[int]], r: int, c: int, color: int, old_color: int) -> None:
        if -1 >= r or r >= self.m or -1 >= c or c >= self.n: return
        if image[r][c] != old_color:
            return
        else:
            image[r][c] = color

        self.dfs(image, r+self.directions[0][0], c+self.directions[0][1], color, old_color)
        self.dfs(image, r+self.directions[1][0], c+self.directions[1][1], color, old_color)
        self.dfs(image, r+self.directions[2][0], c+self.directions[2][1], color, old_color)
        self.dfs(image, r+self.directions[3][0], c+self.directions[3][1], color, old_color)

        