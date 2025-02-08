class Solution(object):
    def merge(self, nums1, m, nums2, n):
        mp= m-1
        np = n-1
        r= m+n-1
        while np>=0:
            if mp>=0 and nums1[mp]> nums2[np]:
                nums1[r] = nums1[mp]
                mp-=1
            else:
                nums1[r] = nums2[np];
                np-=1;
            r-=1;
        return nums1;
        
        