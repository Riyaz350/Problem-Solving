class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        cur =''
        for i in range(len(s)):
            if s[i] != ' ':
                cur+=s[i]
            else:
                if cur:
                    arr.append(cur)
                cur = ''
        arr.append(cur)

        return ''.join([item + ' ' for item in arr[::-1]]).strip()
