from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return f'{len(list(set(nums)))}, nums = {list(set(nums))}'


if __name__ == '__main__':
    print(Solution.removeDuplicates(self=0 , nums= [0,0,1,1,1,2,2,3,3,4]))
