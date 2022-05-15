import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        return collections.Counter(s) == collections.Counter(t)

if __name__ == '__main__':
    print(Solution.isAnagram(0, 'qwe' , 'wwq'))
    print(collections.Counter('qwerty'))
