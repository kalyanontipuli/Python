class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=''
        for x in address:
            if x!='.':
                res=res+x
            else:
                res=res+'[.]'
        return res
