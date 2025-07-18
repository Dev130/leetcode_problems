from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        
        # LEFT: keep smallest sum of n values in first 2n
        left_heap = [-x for x in nums[:n]]  # max-heap (invert sign)
        heapq.heapify(left_heap)
        left_sum = sum(nums[:n])
        left_sums = [left_sum]

        for i in range(n, 2 * n):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(left_heap)  # subtract largest
            left_sums.append(left_sum)

        # RIGHT: keep largest sum of n values in last 2n
        right_heap = nums[2 * n:]
        heapq.heapify(right_heap)  # min-heap
        right_sum = sum(right_heap)
        right_sums = [right_sum]

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            right_sum -= heapq.heappop(right_heap)  # remove smallest
            right_sums.append(right_sum)

        right_sums = right_sums[::-1]

        # Compute minimum difference
        min_diff = float('inf')
        for i in range(n + 1):
            min_diff = min(min_diff, left_sums[i] - right_sums[i])

        return min_diff