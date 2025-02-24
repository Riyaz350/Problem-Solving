class Solution(object):
    def longestConsecutive(self, nums):
        set1 = set(nums)
        ans = 0

        for i in set1:
            if i-1 not in set1:
                count =0
                while i+count in set1:
                    count+=1;
                ans = max(count, ans)
        return ans

        