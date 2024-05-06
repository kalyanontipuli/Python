class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for x in s:
            if x=='(' or x=='{' or x=='[':
                l.append(x)
            elif len(l)>0:
                if x==')' and l[-1]=='(':
                    l.pop(-1)
                elif x=='}' and l[-1]=='{':
                    l.pop(-1)
                elif x==']' and l[-1]=='[':
                    l.pop(-1)
                else:
                    return False
            else:
                return False
        if len(l)==0:
            return True

        
