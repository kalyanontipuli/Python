class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        temp=num
        while num>0:
            r=num%10
            if temp%r==0:
                count+=1
            num=num//10
        return count
        
