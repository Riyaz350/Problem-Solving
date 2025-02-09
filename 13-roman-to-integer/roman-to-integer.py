class Solution(object):
    def romanToInt(self, s):
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000 }
        res = s[::-1]
        sum =dic[res[0]]
        for i in range(1, len(s)):
            if dic[res[i]] < dic[res[i-1]]:
                sum = sum-dic[res[i]]
            else:
                sum = sum+dic[res[i]]
        return sum
        