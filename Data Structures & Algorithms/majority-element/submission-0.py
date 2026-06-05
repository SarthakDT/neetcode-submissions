class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map={}

        for num in nums:
            freq_map[num] = 1 + freq_map.get(num,0)
        
        for num, count in freq_map.items():
            if count > len(nums) // 2:
                return num
        
        return -1