class Solution(object):
    def removeDuplicates(self, nums):
        k = 2;
        ans=2
        for i in range(2, len(nums)):
            if nums[k-2] != nums[i]:
                nums[k] = nums[i]
                k+=1;
                ans+=1
            else:
                continue;
                
        return ans;