class Solution(object):
    def equalPairs(self, grid):
        c = {}
        for i in grid:
            if tuple(i) not in c:
                c[tuple(i)] = 1
            else:
                c[tuple(i)] +=1
        count = 0
        j = 0
        while j< len(grid):
            temp = []
            for k in grid:
                temp.append(k[j])
            if temp in grid:
                count+=c[tuple(temp)]
            j+=1
        return count

        