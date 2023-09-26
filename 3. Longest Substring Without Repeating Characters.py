# PROBLEM
# Given a string s, find the length of the longest substring without repeating characters.


# Solution
def LongestSubstring(s):
    # We want just the unique characters
    unique_set = set(s)
    
    # Convert the set to string
    s = ''.join(unique_set)
    
    # Calculate the length of the string
    length = len(s)
    
    return length

# print(LongestSubstring('aaassssvvvddd'))
print(LongestSubstring('aaaaaaaaaa'))
print(LongestSubstring('aaasssd'))
print(LongestSubstring('aaassssvvvdddffffjjjjskkkkdldlkfsejfoierjfoksd'))

# Another way 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_length = 0
        start = 0
        char_index = {}

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length