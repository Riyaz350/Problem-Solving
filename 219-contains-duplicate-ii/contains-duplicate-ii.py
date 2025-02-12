class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic and abs(dic[num] - i) <= k:
                return True;
            else:
                dic[num] = i;
                    
            
        return False;