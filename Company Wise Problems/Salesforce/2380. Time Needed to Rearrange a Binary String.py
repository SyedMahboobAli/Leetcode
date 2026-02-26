class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeroes = 0
        seconds = 0

        for ch in s:
            if ch == '0':
                zeroes += 1
            elif zeroes > 0:
                seconds = max(seconds+1,zeroes)
        return seconds
