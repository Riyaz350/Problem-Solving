class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in nums1:
            ind = -1
            for  j in range(nums2.index(i), len(nums2)):
                if nums2[j] > i:
                    ind= nums2[j]
                    break
            ans.append(ind)
        return ans