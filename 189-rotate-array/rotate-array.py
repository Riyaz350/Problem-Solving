class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # In case k is larger than the length of nums
        nums[:] = nums[-k:] + nums[:-k]
        return nums