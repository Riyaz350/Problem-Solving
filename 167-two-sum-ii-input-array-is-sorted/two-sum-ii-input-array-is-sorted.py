class Solution(object):
    def twoSum(self, numbers, target):
        dic = {}
        for i,num in enumerate(numbers):
            if target-num not in dic:
                dic[num] = i
            else:
                return [dic[target-num]+1, i+1 ]
        