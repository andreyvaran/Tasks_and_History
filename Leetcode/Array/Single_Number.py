from typing import List
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                temp.remove(i)

        return temp.pop()

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        arr = {}
        for v in nums:
            if v in arr:
                del arr[v]
            else:
                arr[v] = 1
        return list(arr.keys())[0]

class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(0, len(nums), 2):
            try:
                if (nums[i] != nums[i + 1]):
                    return nums[i]
            except:
                return nums[i]


class Solution4:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res



if __name__ == '__main__':
    ls = [4,1,2,1,2]
    print(Solution4.singleNumber(0, ls))