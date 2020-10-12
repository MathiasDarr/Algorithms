class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        k = len(flowerbed)
        count = 0
        for i in range(k):
            if flowerbed[i] ==0:
                if (i==0 or flowerbed[i-1] ==0)  and (i +1 == k or flowerbed[i+1] ==0):
                    count +=1
                    flowerbed[i] =1
            if count >= n:
                return True
        return False


flowerbed = [0,0,1,0,0]
solution = Solution()
solution.canPlaceFlowers(flowerbed, 2)