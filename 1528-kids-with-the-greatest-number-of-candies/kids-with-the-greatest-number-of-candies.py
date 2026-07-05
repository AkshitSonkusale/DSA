class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        l=[]
        maxi=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxi:
                l.append(True)
            else:
                l.append(False)
        return l
            
        