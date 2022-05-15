from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()
        d2 = dict()

        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        res = []
        for k in d1.keys():
            if k in d2:
                res += [k] * min(d1[k], d2[k])
        return res


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()

        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        res = []
        for i in nums2:
            if i in d1:
                res.append(i)
                d1[i] -= 1
                if d1[i] == 0:
                    del d1[i]

        return res


if __name__ == '__main__':
    n1 = [1, 2, 3, 4, 5, 5, 5]
    n2 = [5, 5, 7, 6]
    print(Solution2.intersect(self=0, nums1=n1, nums2=n2))
