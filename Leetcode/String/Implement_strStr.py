class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None:
            return -1

        if haystack == needle:
            return 0

        for i in range(len(haystack) - (ln := len(needle)) + 1):
            if haystack[i:i + ln] == needle:
                return i
        return -1
