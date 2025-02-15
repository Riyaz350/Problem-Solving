class Solution(object):
    def plusOne(self, digits):
        sum= 0
        ans =[]
        div=0
        for i in range(len(digits)):
            sum = sum*10+digits[i];
        sum = sum+1;
        for i in range(len(str(sum))):
            ans.insert(0,int(sum%10))
            sum = sum/10
    
        return ans