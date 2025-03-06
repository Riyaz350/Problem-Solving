class Solution(object):
    def findMaxAverage(self, nums, k):
        cur_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            cur_sum += nums[i]-nums[i-k]
            max_sum = max(cur_sum, max_sum)

        return max_sum/float(k)