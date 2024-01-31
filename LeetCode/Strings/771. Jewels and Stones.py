class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res=0
        for y in stones:
            if y in jewels:
                res+=1
        return res
