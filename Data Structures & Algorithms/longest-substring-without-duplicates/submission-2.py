class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hset=set()
        longest = 0

        for r in range(len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l+=1

            w = r-l+1
            longest=max(w,longest)
            hset.add(s[r])
            r+=1
        
        return longest

