class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d=dict()
        m=-1
        for x in arr:
            if x in d:
                d[x]=d[x]+1
            else:
                d[x]=1
        
        for x in d:
            if d[x]==x:
                m=max(m,x)
        return m
        
