class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        result = []
        n = len(nums)
        start = 0

        for i in range(n):
            if nums[i] == key:
                left = max(0, i - k)
                right = min(n - 1, i + k)

                while start <= right:
                    if start >= left:
                        result.append(start)
                    start += 1

        return result