class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set=sorted(set(nums))

        c=1
        longest=1
        for i in range(len(nums_set)-1):
            if nums_set[i+1]==nums_set[i]+1:
                c+=1

            else:
                longest=max(longest,c)
                c=1
        
        return max(longest,c)