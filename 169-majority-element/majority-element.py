class Solution(object):
    def majorityElement(self, nums):
        count={}
        n=len(nums)
        for num in nums:
            count[num]=count.get(num,0)+1
        for num in count:
            if count[num] > n//2:
                return num
