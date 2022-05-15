import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(' ', '')
        s = re.sub(r"[^A-Za-zА-Яа-я]+", '', s).lower()
        print(s)
        return s == s[::-1]


if __name__ == '__main__':
    o  = Solution
    print(o.isPalindrome(0,"0P"))