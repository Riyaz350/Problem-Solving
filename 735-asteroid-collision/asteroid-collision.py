class Solution(object):
    def asteroidCollision(self, asteroids):
        ans = []
        for i in asteroids:
            while len(ans) and ans[-1] >0 and i <0:
                if  ans[-1] == - i:
                    ans.pop()
                    break
                elif ans[-1] >  -i:
                    break
                elif ans[-1] < -i:
                    ans.pop()
                    continue
                
            else:
                ans.append(i)
        return ans