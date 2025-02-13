class Solution(object):
    def isValid(self, s):
        dic = {')':'(','}':'{',']':'['}
        stk = []
        for c in s:
            if c not in dic:
                stk.append(c)
            else:
                if not stk:
                    return False;
                else:
                    popped = stk.pop()
                    if popped != dic[c]:
                        return False;
        return not stk