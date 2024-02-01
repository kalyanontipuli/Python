class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        i=0
        for word in words:
            if x in word:
                l.append(i)
            i+=1
        return l
