# With hashmap (11ms)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        N, B = len(s1), len(baseStr)
        parent = {}

        # Given x, find its parent
        def find(x):
            parent.setdefault(x, x) # If not assigned already, initialize the parent to be itself
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]


        # Given x, y, make the smaller letter the parent
        def union(x, y):
            # Find out which letter has the smallest equivalent letter
            if find(x) > find(y):
                largerLetter = x
                smallerLetter = y
            else:
                largerLetter = y
                smallerLetter = x
            
            parent[find(largerLetter)] = find(smallerLetter)
            return
        

        # Create groups of letters that are equivalent
        for idx in range(N):
            letter1 = s1[idx]
            letter2 = s2[idx]
            union(letter1, letter2)
        
        # Get the answer in the form of a list of letters
        ansList = ["" for _ in range(B)]
        for idx, letter in enumerate(baseStr):
            # Use find() instead of parent[] since parent is not fully path-compressed
            ansList[idx] = find(letter) 

        return "".join(ansList)