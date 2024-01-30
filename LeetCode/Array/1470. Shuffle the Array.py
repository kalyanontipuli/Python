class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        i=0
        j=n
        while i<n:
            ans.append(nums[i])
            i+=1
            ans.append(nums[j])
            j+=1
        return ans
