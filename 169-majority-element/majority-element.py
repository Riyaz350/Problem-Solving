class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        big= nums[0]
        for i, num in enumerate(nums):
            if num in dic:
                dic[num] += 1;
                if dic[num] > len(nums) / 2:
                    big = num;
            else:
                dic[num]= 1;
        return big