def insert_integer(idx, val, arr):
    if val == 1:
        return 0
    st = str(val)
    for i in range(len(st)):
        arr[idx + i] = st[i]
    return len(st)

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        curr = chars[0]

        kidx = 1

        last = 0

        for i in range(1, len(chars)):
            if chars[i] != curr:
                # Update the count for the character we just finished
                kidx += insert_integer(kidx, i - last, chars)
                # Write the new character
                chars[kidx] = chars[i]
                curr = chars[i]
                kidx += 1
                last = i
        
        # Process the final group
        kidx += insert_integer(kidx, len(chars) - last, chars)

        return kidx