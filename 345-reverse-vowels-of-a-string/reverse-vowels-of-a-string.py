class Solution(object):
    def reverseVowels(self, s):
        v = "aeiouAEIOU"
        chars = list(s)
        left = 0
        right = len(chars) - 1
        while left < right:
            if chars[left] not in v:
                left += 1
            elif chars[right] not in v:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)