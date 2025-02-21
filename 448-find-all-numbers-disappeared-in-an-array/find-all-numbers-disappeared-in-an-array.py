class Solution(object):
    def findDisappearedNumbers(self, nums):
        set1 = set(nums)
        ans = []
        for i in range(len(nums)):
            if i+1 not in set1:
                ans.append(i+1)
        return ans