class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for x in nums:
            s=str(x)
            for y in s:
                l.append(int(y))
        return l
        
