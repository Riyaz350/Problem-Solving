class Solution(object):
    def summaryRanges(self, nums):
        numSet = set(nums)
        s = 0
        i = 0
        ans = []
        while i < len(nums) and s < len(nums):
            if nums[i] + 1 in numSet:
                i += 1
            elif s == i:
                ans.append("{}".format(nums[s]))
                s = i + 1
                i += 1
            else:
                ans.append("{}->{}".format(nums[s], nums[i]))
                s = i + 1
                i += 1
        return ans
