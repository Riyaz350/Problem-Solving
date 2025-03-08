class Solution(object):
    def uniqueOccurrences(self, arr):
        count = Counter(arr)
        s = set()
        for i in count.values():
            if i in s:
                return False
            else:
                s.add(i)
        return True
