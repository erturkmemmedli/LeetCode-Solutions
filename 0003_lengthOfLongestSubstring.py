class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maximum = 0
        start = 0
        end = 0
        dictionary = {}
        for i in range(len(s)):
            if s[i] in dictionary and dictionary[s[i]] + 1 > start:
                start = dictionary[s[i]] + 1
            dictionary[s[i]] = end
            end += 1
            maximum = max(maximum, end - start)
        return maximum

# Alternative solution

class Solution1(object):
    
    def lengthOfLongestSubstring(self, s):
        maximum = 0
        string = ''
        for i in range(len(s)):
            if s[i] not in string:
                string += s[i]
                maximum = max(maximum, len(string))
            else:
                string = string[string.index(s[i]) + 1:]
                string += s[i]
        return maximum

# Alternative solution

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        hashmap = {}
        for i, char in enumerate(s):
            if char not in hashmap:
                hashmap[char] = [i]
            else:
                hashmap[char].append(i)
                start = max(start, hashmap[char][-2] + 1)
            longest = max(longest, i - start + 1)
        return longest
