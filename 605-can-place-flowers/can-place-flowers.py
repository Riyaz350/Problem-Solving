class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in flowerbed:
           
            if i == 0:
                count+=1
            else:
                count=0

            if count== 3:
                if n!= 0:
                    n-=1
                count-=2
        return n==0
