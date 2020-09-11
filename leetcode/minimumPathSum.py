class Solution(object):
    def minPathSum(self, grid):
        m = len(grid[0])
        n = len(grid)

        dp = [[0 for i in range(m)] for j in range(n)]

        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[0][i] += dp[0][i-1] + grid[0][i]

        for i in range(1, n):
            dp[i][0] += dp[i-1][0] + grid[i][0]


        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]


        return dp[n-1][m-1]


sln = Solution()

sln.minPathSum([
  [1,3,1],
  [1,5,1],
[4,2,1]

])