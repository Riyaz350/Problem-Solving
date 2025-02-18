class Solution(object):
    def topKFrequent(self, nums, k):
        dic1 = {}
        ans = [[]  for i in range(len(nums)+1)]

        for i in nums:
            dic1[i]= 1+dic1.get(i,0)
        for i, num in dic1.items():
            ans[num].append(i)

        res = []
        for i in range(len(nums), 0 ,-1):
            for j in ans[i]:
                res.append(j)
                if len(res) == k:
                    return res