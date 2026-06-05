class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        c = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                product = product*nums[i]

            else:
                c+=1
        output = [product]*len(nums)

        if c > 1:
            return [0] * len(nums)

        for i in range(len(output)):
            if nums[i]==0 and c==1:
                output[i] = product
  
            elif nums[i]!=0 and c==0:
                output[i] = output[i]//nums[i]

            elif nums[i]!=0 and c==1:
                output[i]=0
        
        return output