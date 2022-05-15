from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sm = 1
        l = len(nums)
        for i in range(l):
            print(nums)
            if nums[i] == 0:
                nums[i], nums[l - sm] = nums[l - sm], nums[i]
                sm += 1





if __name__ == '__main__':
    nu = [0,1,0,3,12]
    Solution.moveZeroes(self=1 , nums= nu)
    print(nu)