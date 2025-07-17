class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dp = [[0 for _ in range(k)] for _ in range(k)]
        ans = 0

        for num in nums:
            r = num % k
            for j in range(k):
                dp[r][j] = dp[j][r] + 1
                ans = max(ans, dp[r][j])

        return ans