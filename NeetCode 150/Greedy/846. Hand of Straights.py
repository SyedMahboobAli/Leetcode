class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        #count Freq
        count = Counter(hand)
        #process cards in sorted
        for card in sorted(count):
            freq = count[card]
            if freq > 0: #as we keep reducing count
                for i in range(groupSize):
                    if count[card+i] < freq: #since number are consequtive
                        return False
                    count[card+i] -= freq 
        
        return True
