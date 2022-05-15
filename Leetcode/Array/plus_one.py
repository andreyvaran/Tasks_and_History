from typing import List


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        sm = 1
        l = len(digits)
        while c != 0:
            digits[l - sm] += 1
            c = digits[l - sm] // 10
            if c > 0: digits[l - sm] %= 1
            if sm == l and c == 1:
                digits.insert(0, 1)
                return digits
            sm += 1
        return digits


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(reversed(range(len(digits))))
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0

            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits


if __name__ == '__main__':
    digits = [1 , 9,9,9,9,9,9]
    print(Solution2.plusOne(self=0, digits=digits))
