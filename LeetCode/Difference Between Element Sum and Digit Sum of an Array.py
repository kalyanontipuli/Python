class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum=0
        dsum=0
        for x in nums:
            esum=esum+x
            while(x>0):
                r=x%10
                dsum=dsum+r
                x=x//10
        return esum-dsum
        
