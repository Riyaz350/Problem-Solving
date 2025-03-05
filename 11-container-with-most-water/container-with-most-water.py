class Solution(object):
    def maxArea(self, height):
        start = 0
        end =len(height) - 1
        max_area = 0
        while start< end:
            area = abs(start - end) * min(height[start], height[end])
            max_area= max(area, max_area)
            if height[start] < height[end]:
                start+=1
            else:
                end-=1
        return max_area
