class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first = strs[0]

        for i in range(len(first)):
            for s in strs:
                if len(res) >= len(s) or s[i] != first[i]:
                    return res
            res += first[i]
        
        return res