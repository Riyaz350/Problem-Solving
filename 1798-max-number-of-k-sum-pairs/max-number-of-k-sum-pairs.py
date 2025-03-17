class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = Counter(nums)
        seen = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] not in seen and k-nums[i] in c:
                if nums[i] == k - nums[i]:
                    count+=c[nums[i]]//2
                    seen.add(nums[i])
                else:
                    count+=min(c[nums[i]], c[k-nums[i]])  
                    seen.add(nums[i])
                    seen.add(k-nums[i])
        return count