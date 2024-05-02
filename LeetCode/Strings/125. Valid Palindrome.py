class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        for x in s:
            if x.isalpha():
                temp=temp+x.lower()
            elif x.isdigit():
                temp=temp+x
        i=0
        j=len(temp)-1
        while(i<j):
            if temp[i]!=temp[j]:
                return False
            i+=1
            j-=1
        return True
        
