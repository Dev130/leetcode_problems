class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        cand = [1] * n  # Step 1: Initialize each child with 1 candy

        # Step 2: Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                cand[i] = cand[i - 1] + 1

        # Step 3: Right to left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and cand[i] <= cand[i + 1]:
                cand[i] = cand[i + 1] + 1

        # Step 4: Return the sum
        return sum(cand)