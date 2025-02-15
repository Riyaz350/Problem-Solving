class Solution(object):
    def generate(self, numRows):
        ans = []
        if numRows<1:
            return []
        else:
            ans.append([1])
        for i in range(1,numRows):
            temp=ans[i-1][:]
            temp.append(0)
            temp.insert(0,0)
            new = []
            for j in range(i+1):
                new.append(temp[j]+temp[j+1])
            ans.append(new)
        return ans