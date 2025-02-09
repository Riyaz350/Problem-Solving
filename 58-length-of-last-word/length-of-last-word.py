class Solution(object):
    def lengthOfLastWord(self, s):
        last = 0;
        longest = 0
        for i in s:
            if i == " ":
                if last != 0:
                    longest = last;
                last = 0;
            else:
                last +=1;
                longest = last;
                
        return longest;