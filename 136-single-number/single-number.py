class Solution(object):
    def singleNumber(self, nums):
        ans ={}
        for i, num in enumerate(nums):
            if num not in ans:
                ans[num] = i;
            else:
                ans.pop(num)
                
        return list(ans.keys())[0]