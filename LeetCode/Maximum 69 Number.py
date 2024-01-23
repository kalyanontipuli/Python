class Solution:
    def maximum69Number (self, num: int) -> int:
        rnum = int(str(num)[::-1])
        res=''
        while(rnum>0):
            r=rnum%10
            if r==6:
                res=res+'9'
                rnum=rnum//10
                break
            else:
                res=res+'9'
            rnum=rnum//10
        while rnum>0:
            r=rnum%10
            res=res+str(r)
            rnum=rnum//10
        return int(res)


        
