class Solution(object):
    def findDifference(self, nums1, nums2):
        comb = set(nums1+nums2)
        ans = [[],[]]
        for i in comb:
            if i not in nums1 and i in nums2:
                ans[1].append(i)
            elif i not in nums2 and i in nums1:
                ans[0].append(i)
        return ans
        