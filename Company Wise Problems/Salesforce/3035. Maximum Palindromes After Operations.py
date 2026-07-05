'''
Greedy:
Since you can rearrange letters across words, only the total letter counts matter.

For any word of length L:

it needs L // 2 matching pairs,
and if L is odd, it also needs one center letter.

To maximize the number of palindromes:

sort words by length ascending,
satisfy the shortest words first,
track how many pairs and single letters you have available.
'''

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        freq = Counter(ch for w in words for ch in w)

        pairs = sum(v // 2 for v in freq.values())
        singles = sum(v % 2 for v in freq.values())

        ans = 0

        for length in sorted(len(w) for w in words):
            need_pairs = length // 2

            if pairs < need_pairs:
                break

            pairs -= need_pairs #this handles even length scenario

            #for old lengths explanation is below
            if length % 2 == 1:
                if singles > 0:
                    singles -= 1
                else:
                    if pairs == 0:
                        break
                    pairs -= 1
                    singles += 1

            ans += 1

        return ans

'''
old length scenario:
Case 1: We already have a single
if singles > 0:
    singles -= 1

Case 2: No single is available
    if pairs available, Break one pair into two singles, use one as the center, and keep the other for future palindromes.

'''
