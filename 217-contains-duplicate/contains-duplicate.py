class Solution(object):
    def containsDuplicate(self, nums):
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        for num in count:
            if count[num]>=2:
                return True
        return False
        