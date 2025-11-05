class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary where each key is a frequency signature (tuple)
        # and the value is the list of words (strings) that match that signature
        groups = defaultdict(list)
        for s in strs:
            # Initialize an array of length 26 for lowercase English letters
            # Each index represents a character from 'a' to 'z'
            freq = [0] * 26
            for c in s:
                # Count the frequency of each character in the string
                freq[ord(c) - ord('a')] += 1
            # Convert the list to a tuple so it can be used as a hashable dictionary key
            key = tuple(freq)
            groups[key].append(s)
        # Convert the dictionary values to a list of lists (grouped anagrams)
        return list(groups.values())
            
                
