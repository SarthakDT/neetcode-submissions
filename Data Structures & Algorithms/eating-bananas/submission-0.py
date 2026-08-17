class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<=r:
            mid = (l+r)//2

            h_taken = 0
            for p in piles:
                h_taken += (p+mid-1)//mid

            if h_taken>h:
                l=mid+1
            
            else:
                r=mid-1
        
        return l
             
