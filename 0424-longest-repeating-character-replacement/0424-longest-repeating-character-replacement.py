class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        left =0
        max_len =0
        max_freq =0
        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right],0) + 1
            max_freq = max(max_freq, char_count[s[right]])

            if (right - left +1) - max_freq >k:
                char_count[s[left]] -=1
                left +=1

            max_len = max(max_len , right - left +1)
        return max_len

        