class Solution:
    def climbStairs(self, n):
        # if n<=0: return 0
        # elif n==1: return 1
        # elif n==2: return 2
        # else:
        #     return self.climbStairs(n-1) +self.climbStairs(n-2)
        if n<=2: return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1): dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

sol = Solution()
print(sol.climbStairs(5))
print(sol.climbStairs(-1))
print(sol.climbStairs(8))
print(sol.climbStairs(2))
print(sol.climbStairs(3))