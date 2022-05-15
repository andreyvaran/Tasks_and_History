from typing import List

class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = dict()

        for i in nums:
            if i in temp.keys():
                temp[i] +=1
            else :
                temp[i] = 1
        return any(val >=2 for val in temp.values())


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()

        for i in nums:
            if i in temp:
                return True
            else:
                temp.add(i)
        return False

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution1.containsDuplicate( 0, nums))