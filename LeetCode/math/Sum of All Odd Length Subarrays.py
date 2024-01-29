class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sum=0
        l=len(arr)
        for size in range(1,l+1,2):
            for i in range(0,l-size+1,1):
                for j in range(i,i+size,1):
                    sum=sum+arr[j]
        return sum
        
