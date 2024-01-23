class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while(num>0):
            if num%2==0:
                num=num//2
