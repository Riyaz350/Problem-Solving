class Solution(object):
    def longestOnes(self, nums, k):
        zeros = 0
        l= 0
        max_ones = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros +=1
            while zeros > k:
                if nums[l] == 0:
                    zeros-=1
                l+=1
            w = r-l+1
            max_ones = max(w, max_ones)
        return max_ones