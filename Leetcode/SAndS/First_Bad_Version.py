first_bad = 0


def isBadVersion(version):
    if version >= first_bad:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start


class Solution2:
    def firstBadVersion(self, n):
        if n < 2:
            return n
        start = 1
        end = n
        while (start <= end):
            mid = (start + end) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid - 1):
                end = mid - 1
            else:
                start = mid + 1
