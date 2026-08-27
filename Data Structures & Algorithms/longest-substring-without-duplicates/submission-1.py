class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encmp = {}
        l=0
        res=0

        for r in range(len(s)):
            if s[r] in encmp:
                l=max(encmp[s[r]]+1,l)
            encmp[s[r]]=r
            res = max(res,r-l+1)
        
        return res
