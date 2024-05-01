class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<2:
            return True
        else:
            fl=word[0]
            sl=word[1]
            if ord(fl)<97 and ord(sl)<97:
                for x in word:
                    if ord(x)>=97:
                        return False
                return True

            elif ord(fl)<97:
                for i in range(1,len(word)):
                    x=word[i]
                    if ord(x)<97:
                        return False
                return True
            else:
                for x in word:
                    if ord(x)<97:
                        return False
                return True
