class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        arr = []
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            arr.append((s[i], j - i))
            i = j

        maximillian = 0

        for i in range(len(arr)):
            start = arr[i][0]
            count = 0
            j = i
            remaining = k
            while j < len(arr):
                # first add the current (self explanatory)
                if arr[j][0] == start:
                    count += arr[j][1]
                else:
                    if arr[j][1] > remaining:
                        count += remaining
                        remaining = 0
                        break
                    else:
                        remaining -= arr[j][1]
                        count += arr[j][1]
                j += 1
            count = min(count + remaining, len(s))
            maximillian = max(maximillian, count)

        return maximillian