class Solution(object):
    def thirdMax(self, nums):
        set1 = set(nums)
        if len(set1) <3:
            return max(set1)
        ans =[]
        max1=float('-inf')
        max2=float('-inf')
        max3=float('-inf')
        for i in set1:
            if  i > max1:
                max3= max2;
                max2=max1
                max1=i;
            elif i>max2 :
                max3=max2;
                max2=i;
            elif i > max3:
                max3 = i;
        last = max3
        return last