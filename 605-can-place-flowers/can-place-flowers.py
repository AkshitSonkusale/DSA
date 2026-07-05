class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            # check three things:
            #   current empty?     flowerbed[i] == 0
            #   left empty/edge?   i == 0 or flowerbed[i-1] == 0
            #   right empty/edge?  i == len(flowerbed)-1 or flowerbed[i+1] == 0
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1     # plant here so the next plot sees it
                count += 1
        return count >= n