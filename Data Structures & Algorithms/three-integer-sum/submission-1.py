class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)

        result = []

        for i in range(n):
            l=i+1
            r=n-1

            while l<r:
                
                sum=nums[l]+nums[r]

                if -1*nums[i]==sum:
                    triplet=[nums[i],nums[l],nums[r]]
                    if triplet not in result:
                        result.append(triplet)
                    
                    l+=1
                    r-=1

                elif -1*nums[i]<sum:
                    r-=1
                
                elif -1*nums[i]>sum:
                    l+=1
        
        return result

