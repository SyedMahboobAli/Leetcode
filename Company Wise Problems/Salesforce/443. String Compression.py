'''
Idea

Use two pointers:

one pointer to read the input,
one pointer to write the compressed result in-place.

For each group of repeated characters:

write the character once,
if the count is greater than 1, write the digits of the count.


'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0 
        read = 0
        n = len(chars)

        while read < n:
            current = chars[read]
            count = 0

            while read < n and chars[read] == current:
                read += 1
                count += 1
            
            chars[write] = current
            write += 1

            if count>1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write
