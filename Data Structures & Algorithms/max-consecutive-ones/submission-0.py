class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_ret = 0, 0

        for number in nums:
            if number == 1:
                count += 1
            else:
                count = 0
            max_ret = max(count, max_ret)
        return max_ret
            
