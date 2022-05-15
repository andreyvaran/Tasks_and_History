from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1 решение
        '''
        res = 0
        # temp = prices[0]
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i] :
                res += prices[i+1] - prices[i]

        return res

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        2 решение
        '''
        res = 0
        temp = prices[0]
        for i in range(1,len(prices)-1):
            if prices[i] > temp :
                res += prices[i] - temp
                temp=prices[i]

        return res




if __name__ == '__main__':
    lst = []
    print(Solution.maxProfit(0, lst))