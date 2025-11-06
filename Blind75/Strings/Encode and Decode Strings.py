class Solution:
    # Encodes a list of strings to a single string.
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    # Decodes a single string to a list of strings.
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find delimiter #. This uses a while loop to handle more than one digit length
            #Encoded string = "4#leet4#code"
            #                  ↑↑
            #                  ij
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # get length
            word = s[j + 1:j + 1 + length]  # get the actual string
            res.append(word)
            i = j + 1 + length  # move pointer
        return res
