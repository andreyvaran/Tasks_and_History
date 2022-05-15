from typing import List


class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(k):
            temp = nums.pop(len(nums) - 1)
            nums.insert(0, temp)


class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """

        """
        ln = len(nums)
        nums[::]=nums[ln-k%ln:ln]+nums[0:ln-k%ln]
        return nums

class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        O(2n) time o(n) space
        """
        l = len(nums)
        if k % l == 0:
            nums = nums[::-1]
        else:
            k = k % l
            temp = nums[::]
            for i in range(l):
                index = (i + k) % l
                temp[index] = nums[i]
            nums = temp[::]
        return nums


class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        o(2n) time O(1) space
        """
        ln = len(nums)
        k = k % ln
        # print(nums)
        nums.reverse()
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            # print(f'here l  = {l} , r = {r}')
        # print(nums)
        l, r = k, ln-1
        while k < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # print(nums)
        return nums


if __name__ == '__main__':
    # nums = [-1, -100, 3, 99]
    # k = 2
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 5
    print(Solution4.rotate(0, nums=nums, k=k))
