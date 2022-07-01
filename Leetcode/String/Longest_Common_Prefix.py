from typing import  List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        shortest = strs[0]
        prefix = ''
        for i in range(len(shortest)):
            if strs[len(strs) - 1][i] == shortest[i]:
                prefix += strs[len(strs) - 1][i]
            else:
                break
        return prefix


class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        answer = ""
        while True:
            if i < len(strs[0]):
                temp = strs[0][i]
            else:
                break
            for s in strs:
                if i >= len(s) or s[i] != temp:
                    break
            else:
                answer += temp
                i += 1
                continue
            break
        return answer