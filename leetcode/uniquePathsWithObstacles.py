class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = 0

        dp = [[0 for j in range(0, n)] for i in range(0, m)]

        if (obstacleGrid[0][0] == 1):
            return 0
        else:
            dp[0][0] = 1

        for i in range(1, n):
            if (obstacleGrid[0][i] == 1):
                break
            else:
                dp[0][i] = 1
        
        for i in range(1, m):
            if (obstacleGrid[i][0] == 1):
                break
            else:
                dp[i][0] = 1

        

        for i in range(1, m):
            for j in range(1, n):
                if (obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


sln = Solution()

print(sln.uniquePathsWithObstacles([
  [1, 0]
]))