class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            b=i+1;
            while(b < len(nums)):
                if nums[i] + nums[b] == target:
                    return [i,b]
                else:
                    b+=1;