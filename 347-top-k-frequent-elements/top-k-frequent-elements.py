class Solution(object):
    def topKFrequent(self, nums, k):
        ans = []
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num]=1;
            else:
                dict1[num] +=1
        for i in range(k):
            maxVal= max(dict1.values())
            key = [k for k, v in  dict1.items() if v == maxVal][0]
            
            ans.append(key)
            dict1.pop(key)
        return ans