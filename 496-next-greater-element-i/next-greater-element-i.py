class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        dic = {}
        ans = []
        for i, num in enumerate(nums2):
            if num not in dic: dic[num] = i;
        for i in nums1:
            ind = -1
            for  j in range(dic[i], len(nums2)):
                if nums2[j] > i:
                    ind= nums2[j]
                    break
            ans.append(ind)
        return ans