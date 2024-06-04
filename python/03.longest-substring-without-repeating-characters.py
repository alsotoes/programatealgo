class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        maxLen = 0
        charCount = {}

        for right in range(len(s)):
            charCount[s[right]] = charCount.get(s[right], 0) + 1

            while charCount[s[right]] > 1:
                charCount[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen
