import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(' ', '')
        s = re.sub(r"[^A-Za-zА-Яа-я0-9]+", '', s).lower()
        return s == s[::-1]
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        # s = s.replace(' ', '')
        s = list(filter(str.isalnum , s))
        return s == s[::-1]


if __name__ == '__main__':
    o  = Solution2
    print(o.isPalindrome(0,"aseefa"))