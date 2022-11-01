class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:        
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, len(obstacleGrid)):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
        for j in range(1, len(obstacleGrid[0])):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1 - obstacleGrid[0][j])
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]

# Alternative solution

class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
