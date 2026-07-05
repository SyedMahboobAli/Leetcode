'''Instead of simulating every second, count how long each '1' needs to move past the '0's before it.

Observation
Every '1' must cross all preceding '0's.
Let:
zeros = number of '0's seen so far.
time = minimum seconds required so far.

When we encounter a '1':

If there are no preceding zeros, it doesn't need to move.
Otherwise:
It needs at least zeros swaps.
But if the previous '1' is still moving, this '1' must wait.
Hence:
time = max(time + 1, zeros)
imagine for 0111 to understand the logic
'''
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
