class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        oddEven=[-100, 0]
        for f in freq.values():
            f=-f if (f&1)==0 else f
            oddEven[f&1]=max(f, oddEven[f&1])
        return sum(oddEven)