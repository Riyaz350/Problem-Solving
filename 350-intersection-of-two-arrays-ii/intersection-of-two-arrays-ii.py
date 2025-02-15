class Solution(object):
    def intersect(self, nums1, nums2):
        dic1 = {}
        ans= []
        for i, num in enumerate(nums1) :
            if num not in dic1:
                dic1[num] = 1;
            else:
                dic1[num] = dic1[num]+1
        for i, num in enumerate(nums2):
            if num in dic1:
                if dic1[num] != 0:
                    dic1[num] -=1;
                    ans.append(num)
        return ans