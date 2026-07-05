class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i, n = 0, len(s)
        while i < n:
            if s[i] != ' ':
                start = i
                while i < n and s[i] != ' ':
                    i += 1
                words.append(s[start:i])
            else:
                i += 1
        return " ".join(reversed(words))