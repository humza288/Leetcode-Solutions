class Solution(object):
    def uniquePaths(self, m, n):
        
        dp = 0

        dp = [[0 for j in range(0, n)] for i in range(0, m)]

        dp[0][0] = 1

        for i in range(1, n):
            dp[0][i] = 1
        
        for i in range(1, m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


sln = Solution()

print(sln.uniquePaths(7, 3))