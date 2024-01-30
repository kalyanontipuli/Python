class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res=0
        for x in operations:
            if x=="++X":
                res=res+1
            elif x=="X++":
                res=res+1
            elif res=="--X":
                res=res-1
            else:
                res=res-1
        return res

        
