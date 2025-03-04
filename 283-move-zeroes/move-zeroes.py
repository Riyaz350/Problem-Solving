class Solution(object):
    def moveZeroes(self, nums):
        i = 0

        for j in range(1, len(nums)):
            if nums[i]!=0:
                i+=1;
                continue;
            elif nums[j]:
                nums[i], nums[j]= nums[j], nums[i]
                i+=1;

        return nums