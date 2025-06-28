import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        heapq.heapify(arr)
        for i in range(len(nums)):
            heapq.heappush(arr,[nums[i],i])
            if len(arr)>k:
                heapq.heappop(arr)
        def f(d):
            return d[1]
        arr = sorted(arr,key = f)
        ans = []
        for i in range(len(arr)):
            ans.append(arr[i][0])
        return ans