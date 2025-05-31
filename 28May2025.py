class Solution:
    def maxTargetNodes(self, e1: List[List[int]], e2: List[List[int]], k: int) -> List[int]:
        def build(e: List[List[int]], k: int) -> List[int]:
            def dfs(node: int, par: int, k: int) -> int:
                return k>=0 and sum(dfs(ch,node,k-1) for ch in chldn[node] if ch!=par)+1

            chldn = defaultdict(list)
            for u,v in e:
                chldn[u].append(v);chldn[v].append(u)

            return [dfs(i,-1,k) for i in range(len(e)+1)]

        return [*map(add,build(e1,k),repeat(max(build(e2,k-1))))]