from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i,val in enumerate(nums):
            diff = target - val
            if diff in checker:
                return [checker[diff],i]
            checker[val] = i
        return


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ost = dict()

        for i in range(len(nums)):
            if nums[i] in ost:
                return [ost[nums[i]], i]
            else:
                ost[target - nums[i]] = i

