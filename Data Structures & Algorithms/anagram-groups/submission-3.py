class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res1 = []
        res2 = {}

        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))

            if key not in res2:
                res2[key] = []

            res2[key].append(strs[i])

        return list(res2.values())
