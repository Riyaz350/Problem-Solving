class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxVal =0;
        ans = 0
        for i in nums:
            if i == 1:
                ans+=1;
            else:
                maxVal= max(ans, maxVal)
                ans=0
        maxVal = max(ans, maxVal)
        return maxVal;
        