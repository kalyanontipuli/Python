class Solution:
    def addDigits(self, num: int) -> int:
        while  num>=9:
            num=Solution.digitsSum(num)
        return num
    @staticmethod
    def digitsSum(num):
        res=0
        while num>0:
            res=res+num%10
            num=num//10
        return res
