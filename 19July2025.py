class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        prev_slash = folder[0] + '/'
        for path in folder[1:]:
            if not path.startswith(prev_slash):
                res.append(path)
                prev_slash = path + '/'
        return res